"""云服务器成本估算小工具。

根据实例规格、实例数量与购买月数，估算云服务器的月度费用和总费用。
仅使用 Python 标准库，直接运行即可。
"""

# 规格名称 -> (CPU 核数, 内存 GB, 每月单价/元)
SPECS = {
    "1": ("1C2G", 1, 2, 45.0),
    "2": ("2C4G", 2, 4, 88.0),
    "3": ("4C8G", 4, 8, 176.0),
    "4": ("8C16G", 8, 16, 352.0),
}


def show_specs():
    """打印可选规格列表。"""
    print("可选实例规格：")
    print(f"{'编号':<6}{'规格':<8}{'CPU':<6}{'内存(GB)':<10}{'月单价(元)':<10}")
    for key, (name, cpu, mem, price) in SPECS.items():
        print(f"{key:<8}{name:<8}{cpu:<6}{mem:<12}{price:<10.2f}")


def read_positive_int(prompt):
    """读取一个正整数，输入非法时要求重新输入。"""
    while True:
        raw = input(prompt).strip()
        if not raw.isdigit() or int(raw) <= 0:
            print("输入无效，请输入大于 0 的整数。")
            continue
        return int(raw)


def calc_cost(monthly_price, count, months):
    """计算总费用：月单价 × 实例数量 × 月数。"""
    return monthly_price * count * months


def main():
    print("=" * 46)
    print("        云服务器成本估算工具 v1.0")
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
    count = read_positive_int("请输入实例数量：")
    months = read_positive_int("请输入购买月数：")

    monthly_total = monthly_price * count
    total = calc_cost(monthly_price, count, months)

    print("\n---------------- 估算结果 ----------------")
    print(f"实例规格：{name}（{cpu} 核 / {mem} GB）")
    print(f"实例数量：{count} 台")
    print(f"购买时长：{months} 个月")
    print(f"每月费用：{monthly_total:.2f} 元")
    print(f"总费用  ：{total:.2f} 元")
    print("------------------------------------------")


if __name__ == "__main__":
    main()
