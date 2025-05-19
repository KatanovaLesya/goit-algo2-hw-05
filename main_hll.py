from log_analyzer import extract_ips_from_log, count_unique_ips_exact, count_unique_ips_hll

if __name__ == "__main__":
    log_file_path = "lms-stage-access.log"

    print("Завантаження лог-файлу...")
    ip_list = extract_ips_from_log(log_file_path)
    print(f"Загальна кількість IP-адрес у файлі: {len(ip_list)}")

    print(ip_list[:5])

    print("\n🔎 Точний підрахунок...")
    exact_count, exact_time = count_unique_ips_exact(ip_list)

    print("⚡ Підрахунок через HyperLogLog...")
    hll_count, hll_time = count_unique_ips_hll(ip_list)

    print("\n📊 Результати порівняння:")
    print(f"{'Метод':<30}{'Унікальні елементи':<25}{'Час виконання (сек.)'}")
    print("-" * 70)
    print(f"{'Точний підрахунок':<30}{exact_count:<25}{exact_time:.4f}")
    print(f"{'HyperLogLog':<30}{hll_count:<25}{hll_time:.4f}")
    print("-" * 70)

    relative_error = abs(exact_count - hll_count) / exact_count * 100
    print(f"\n📉 Похибка HyperLogLog: ~{relative_error:.2f}%")
