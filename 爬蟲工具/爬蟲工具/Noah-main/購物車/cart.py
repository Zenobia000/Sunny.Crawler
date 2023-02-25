 
# 購物車
# 商品名稱：key,商品數量：value
shoppingcar = {}
 
# 添加商品
def addproduct(product, num):
    if num.isdigit():  # isdigit()如果字符串只包含數字則返回 True 否則返回 False。
        num = int(num)
        # 判断key是否存在
        if product not in shoppingcar:
            shoppingcar[product] = num
        else:
            # 修改指定键的值
            shoppingcar[product] += num
        print("商品添加成功")
    else:
        print("數量輸入錯誤")
 
# 删除商品
def delproduct(name, num):
    product = 0
    for key in shoppingcar:
        if key[0] == name:
            product = key
    if num.isdigit():
        num = int(num)
        if num >= shoppingcar[product]:
            for product in shoppingcar:
                if product[0] == name:
                    # 刪除該商品的全部
                    shoppingcar.pop(product)
        else:
            # 刪除該商品指定的數量【修改value值】
            shoppingcar[product] -= num
 
        print("商品删除成功")
    else:
        print("數量輸入錯誤")
 
 
if __name__ == '__main__':
    print("**********歡迎進入NoaH超市**********")
    saving = input("請輸入您的金額：")
 
    if saving.isdigit():
        saving = int(saving)
        while True:
            print("可以進行的操作如下：\n "
                  "0.添加商品  1.删除商品  2.購物車結帳  3.離開超市")
            choice = input("請輸入您的需求是：")
 
            if choice in ["0", "1", "2", "3"]:
 
                if choice == '0':
                    # 添加
                    # 儲存商品的列表
                    product_list = [
                        ('book', 88),
                        ('iphone', 8888),
                        ('food', 100),
                        ('lighter', 500),
                        ('computer', 7000)
                    ]
                    # 展示商品内容
                    print("本商店的商品如下：")
                    for i, goods in enumerate(product_list):
                        print("%d:%s" % (i, goods))
 
                    index = input("請輸入你需要購買的商品編號：")
 
                    if index.isdigit():
                        index = int(index)
                        if 0 <= index <= len(product_list) - 1:
                            product = product_list[index]
 
                            num = input("請輸入需要購買的%s的数量：" % (product[0]))
 
                            if int(num) * product[1] > saving:
                                print("金額不足")
                                saving += int(input("請輸入需要增加的金额："))
                                print("充值成功，余额为：%d" % saving)
                            else:
                                # 減去商品價格
                                saving -= int(num) * product[1]
                                # 將商品添加到購物車
                                addproduct(product, num)
                    else:
                        print("商品的編號輸入有誤")
 
                elif choice == '1':
                    # 刪除
                    name = input("請輸入需要删除的商品名稱：")
                    num = input("請輸入需要删除的商品的數量：")
                    for product in shoppingcar:
                        if product[0] == name:
                            # 添加金額
                            saving += int(num) * product[1]
                    delproduct(name, num)
 
                elif choice == '2':
                    # 結算購物車
                    print("----------你已經購買了如下商品----------")
                    for key,value in shoppingcar.items():
                        print("%s:%s"%(key,value))
 
                    # 清空購物車
                    shoppingcar.clear()
                    print("你還剩餘%d元" % saving)
 
                else:
                    # 退出
                    print("歡迎下次光臨")
                    break
            else:
                print("目前尚未有此功能")
    else:
        print("金額輸入錯誤，請重新輸入")