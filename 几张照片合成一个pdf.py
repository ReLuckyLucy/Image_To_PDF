from PIL import Image
import os
 
 
def rea(path, pdf_name):    # path为图片文件夹路径，pdf_name为输出文件名
    file_list = os.listdir(path)    # 获取文件夹下所有文件名
    pic_name = []   # 存放图片名
    im_list = []    # 存放图片
    for x in file_list:    # 遍历文件夹下所有文件名
        if "jpg" in x or 'png' in x or 'jpeg' in x:     # 判断是否为图片
            pic_name.append(x)  # 将图片名添加到pic_name列表中
    
    pic_name.sort()    # 对图片名进行排序
    new_pic = []    # 存放排序后的图片名
    
    for x in pic_name:  # 遍历图片名
        if "jpg" in x:  # 判断是否为jpg格式
            new_pic.append(x)   # 将图片名添加到new_pic列表中
    
    for x in pic_name:  # 遍历图片名
        if "png" in x:  # 判断是否为png格式
            new_pic.append(x)   # 将图片名添加到new_pic列表中
 
    print("hec", new_pic)   # 打印排序后的图片名
 
    im1 = Image.open(os.path.join(path, new_pic[0]))    # 打开第一张图片   
    new_pic.pop(0)  # 将第一张图片从new_pic列表中删除
    for i in new_pic:       # 遍历图片名
        img = Image.open(os.path.join(path, i))     # 打开图片
        # im_list.append(Image.open(i))
        if img.mode == "RGBA":  # 判断图片模式是否为RGBA
            img = img.convert('RGB')    # 将图片模式转换为RGB
            im_list.append(img)    # 将图片添加到im_list列表中
        else:   # 如果图片模式不是RGBA
            im_list.append(img)   # 将图片添加到im_list列表中
    im1.save(pdf_name, "PDF", resolution=100.0, save_all=True, append_images=im_list)   # 保存图片为PDF格式
    print("输出文件名称：", pdf_name)   # 打印输出文件名称
    
 
if __name__ == '__main__':
 
    pdf_name = 'data.pdf'   # 输出文件名
    mypath=r"out"  # 图片文件夹路径
    if ".pdf" in pdf_name:  # 判断输出文件名是否为pdf格式
        rea(mypath, pdf_name=pdf_name)  # 调用rea函数
    else:   # 如果输出文件名不是pdf格式
        rea(mypath, pdf_name="{}.pdf".format(pdf_name))  # 调用rea函数
