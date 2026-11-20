"""云服务器成本估算小工具 v2.0。

根据实例规格、实例数量、数据盘容量与购买月数，估算云服务器的费用，
并支持包年/半年折扣。仅使用 Python 标准库，直接运行即可。
"""

# 规格名称 -> (CPU 核数, 内存 GB, 每月单价/元)
SPECS = {
    "1": ("1C2G", 1, 2, 45.0),
    "2": ("2C4G", 2, 4, 88.0),
    "3": ("4C8G", 4, 8, 176.0),
    "4": ("8C16G", 8, 16, 352.0),
}

# 云盘单价：元 / GB / 月
DISK_PRICE_PER_GB = 0.35


def show_specs():
    """打印可选规格列表。"""
    print("可选实例规格：")
    print(f"{'编号':<6}{'规格':<8}{'CPU':<6}{'内存(GB)':<10}{'月单价(元)':<10}")
    for key, (name, cpu, mem, price) in SPECS.items():
        print(f"{key:<8}{name:<8}{cpu:<6}{mem:<12}{price:<10.2f}")


def read_int(prompt, allow_zero=False):
    """读取整数，allow_zero 为 True 时允许输入 0。"""
    while True:
        raw = input(prompt).strip()
        if not raw.isdigit():
            print("输入无效，请输入非负整数。")
            continue
        value = int(raw)
        if value == 0 and not allow_zero:
            print("输入无效，请输入大于 0 的整数。")
            continue
        return value


def get_discount(months):
    """按购买时长返回 (折扣系数, 折扣说明)。"""
    if months >= 12:
        return 0.85, "包年 8.5 折"
    if months >= 6:
        return 0.95, "半年 9.5 折"
    return 1.0, "无折扣"


def calc_cost(monthly_price, count, months, disk_gb=0):
    """计算费用，返回 (每月费用, 折后总费用, 折扣系数)。"""
    monthly = (monthly_price + disk_gb * DISK_PRICE_PER_GB) * count
    discount, _ = get_discount(months)
    total = monthly * months * discount
    return monthly, total, discount


def main():
    print("=" * 46)
    print("        云服务器成本估算工具 v2.0")
    print("=" * 46)

    show_specs()

    while True:
        choice = input("\n请选择规格编号（直接回车退出）：").strip()
        if choice == "":
            print("已退出。")
            return
        if choice in SPECS:
            break
        print("没有该编号，请重新选择。")

    name, cpu, mem, monthly_price = SPECS[choice]
    count = read_int("请输入实例数量：")
    disk_gb = read_int("请输入每台数据盘容量(GB，没有填 0)：", allow_zero=True)
    months = read_int("请输入购买月数：")

    monthly_total, total, discount = calc_cost(monthly_price, count, months, disk_gb)
    _, discount_text = get_discount(months)

    print("\n---------------- 估算结果 ----------------")
    print(f"实例规格：{name}（{cpu} 核 / {mem} GB）")
    print(f"实例数量：{count} 台")
    print(f"数据盘  ：{disk_gb} GB/台（{DISK_PRICE_PER_GB:.2f} 元/GB/月）")
    print(f"购买时长：{months} 个月（{discount_text}）")
    print(f"每月费用：{monthly_total:.2f} 元")
    print(f"总费用  ：{total:.2f} 元")
    print("------------------------------------------")


if __name__ == "__main__":
    main()
