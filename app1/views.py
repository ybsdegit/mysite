from django.shortcuts import render, HttpResponse, redirect
from app1.models import User, Press, Book, Author
from django.conf import settings
import os


def login(request):
    print(request.GET)
    print('-' * 120)
    error_msg = ''
    # 需要判断
    # 根据请求的方法来做判断
    if request.method == 'POST':
        # 如果是第二次来，表示填完了要给我发数据了             --> POST
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        print(email, pwd)
        # if email == '1@1.com' and pwd == '123':
        # 从数据库查询有没有这个用户
        # select * from app01_user where email='1@1.com' and pwd='123';
        ret = User.objects.filter(email=email, pwd=pwd)
        if ret:
            # 登录成功
            # 跳转到路飞学城
            # return redirect('https://www.luffycity.com')
            # return render(request, 'index.html')
            return redirect('/index/')
        else:
            # 登录失败
            # 提示用户邮箱或密码错误
            error_msg = '邮箱或密码错误'
    # 如果你是第一次来，是跟我要一个登录页面用来填写数据的  --> GET
    return render(request, 'login.html', {'error_msg': error_msg})


# def yingying(request):
#     # 拿到用户发过来的数据
#     print(request.POST)
#     # request.POST['email']
#     email = request.POST.get('email')
#     pwd = request.POST.get('pwd')
#     print(email, pwd)
#     if email == '1@1.com' and pwd == '123':
#         # 登录成功
#         # 跳转到路飞学城
#         # return redirect('https://www.luffycity.com')
#         # return render(request, 'index.html')
#         return redirect('/index/')
#     else:
#         # 登录失败
#         # 提示用户邮箱或密码错误
#         pass
#     return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')


def press_list(request):
    """
    出版社列表
    1. 去数据库查所有的出版社
    2. 在HTML页面展示
    """
    ret = Press.objects.all().order_by('id')
    # print(ret)
    # return HttpResponse('OK')
    return render(request, 'press_list2.html', {'kangchen': ret})


def add_press(request):
    """
    添加出版社
    :param request:
    :return:
    """
    if request.method == "POST":
        # 表示用户填写完了，要给我发数据
        # 1. 取到用户填写的出版社数据
        press_name = request.POST.get('name')
        # 2. 将数据添加到数据库中
        Press.objects.create(name=press_name)
        # 3. 跳转到出版社列表页面
        return redirect('/press_list/')
    # 1. 返回一个输入页面，让用户在上面填写新的出版社信息
    return render(request, 'add_press2.html')


def delete_press(request):
    """删除出版社"""
    # 1. 获取要删除的出版社id
    delete_id = request.GET.get('id')
    # 2. 根据id去数据库删除对应的数据行
    Press.objects.filter(id=delete_id).delete()
    # 3. 让用户再去访问列表页
    return redirect('/press_list/')


def edit_press(request):
    """编辑出版社"""
    # 从url中获取要编辑的出版社id  request.GET从url中获取参数
    edit_id = request.GET.get('id')
    if request.method == "POST":
        # 用户修改完出版社信息给我发过来了
        # 1. 取出用户编辑后的数据
        # edit_id = request.POST.get('id')
        
        new_name = request.POST.get('name')
        # 2. 去数据库修改对应的数据
        # 2.1 先找出对应的数据
        edit_press_obj = Press.objects.get(id=edit_id)
        # 2.2 修改出版社的名称
        edit_press_obj.name = new_name  # 这一步只发生在ORM实例对象层面
        # 2.3 将修改同步到数据库
        edit_press_obj.save()
        # 让用户再去访问出版社列表页
        return redirect('/press_list/')
    
    # 1. 获取要编辑的出版社id
    # edit_id = request.GET.get('id')
    # 2. 获取该出版社的信息
    # ret = Press.objects.filter(id=edit_id)  -->[Press obj]
    ret = Press.objects.get(id=edit_id)  # --> Press obj get()有且只有一个对象，否则就报错
    # 3. 在页面上展示出来
    return render(request, 'edit_press2.html', {'press_obj': ret})


def book_list(request):
    """书籍列表"""
    # 1. 查询所有的书籍数据
    data = Book.objects.all()
    # print(data[0].press.name)
    # 2. 在页面上展示出来
    # 3. 返回完成的HTMl
    return render(request, 'book_list2.html', {'data': data})


def add_book(request):
    """添加书籍"""
    # 1. 返回一个页面，让用户添加书籍信息
    # 因为书籍信息要关联出版社，
    # 所以，再添加属鸡的页面要把已经存在的出版社展示出来， 让用户选择
    if request.method == "POST":
        book_title = request.POST.get('book_title')
        press_id = request.POST.get('press_id')
        book_price = request.POST.get('book_price')
        # 创建新的书籍记录
        # 基于对象的创建
        # press_obj = Press.objects.get(id=press_id)
        # Book.objects.create(title=book_title, press=press_obj )
        # 基于外键id的创建
        Book.objects.create(title=book_title, price=book_price, press_id=press_id)
        return redirect('/book_list/')
    
    press_data = Press.objects.all()
    return render(request, 'add_book2.html', {'press_list': press_data})


def delete_book(request):
    """添加书籍"""
    # 1. 从url获取现有删除书籍的id
    delete_book_id = request.GET.get('id')
    # 2. 根据id值去数据库找到对应的数据，删除
    Book.objects.filter(id=delete_book_id).delete()
    # 3. 跳转到书籍列表页面
    
    return render(request, 'delete_success.html')
    # return redirect('/book_list/')  # 给浏览器返回一个特殊的响应（命令），访问指定的URL


def edit_book(request):
    """编辑书籍"""
    # 1. 从 URL 中取到要编辑书籍的id
    edit_book_id = request.GET.get('id')
    # 2. 根据id值找到要编辑的书籍对象
    edit_book_obj = Book.objects.get(id=edit_book_id)
    
    if request.method == 'POST':
        # 1. 取到用户修改后的书籍名称和出版社信息
        new_title = request.POST.get('book_title')
        new_price = request.POST.get('book_price')
        new_press_id = request.POST.get('press_id')
        # 2. 获取到要编辑的出版社对象
        # 3. 修改书籍相应信息
        edit_book_obj.title = new_title
        edit_book_obj.price = new_price
        edit_book_obj.press_id = new_press_id
        # 4. 保存到数据库
        edit_book_obj.save()
        # 5. 跳转到书籍列表页
        return redirect('/book_list/')
    
    # 2.1 把所有的出版社信息查取出来
    press_data = Press.objects.all()
    # 3. 在页面显示当前书籍的信息，等待被编辑
    return render(request, 'edit_book2.html', {
        'edit_book_obj': edit_book_obj,
        'press_list': press_data})


def author_list(request):
    """作者列表"""
    # 1. 取数据库查询到所有的作者
    author_data = Author.objects.all()
    for author in author_data:
        print(author)
        # 取到每个作者出版的所有书籍
        print(author.books)  # 是一个ORM提供的桥梁（工具），帮我找对应关系
        print(author.books.all())
    # 2. 在页面上展示出来
    return render(request, 'author_list.html', {'author_list': author_data})
    # return HttpResponse('ok')


def add_author(request):
    """添加作者"""
    # 1. 返回一个页面给用户，让用户填写作者信息
    # 2. 获取所有的书籍信息
    if request.method == "POST":
        # 1. 取到用户填写的信息
        new_author = request.POST.get('author_name')
        # book_ids = request.POST.get('books')  # get() 只能获取到一个值
        book_ids = request.POST.getlist('books')  # getlist() 能获取到所有值
        # print(new_author, book_ids)
        # 2. 添加到数据库
        # 2.1 创建新的作者
        author_obj = Author.objects.create(name=new_author)
        # 2.2 创建新的作者和书的对应关系
        author_obj.books.add(*book_ids)  # ‘*’ 打散传值，参数是一个一个单独的id
        # Author_obj.books.set(book_ids)  # id值的列表
        # 3. 跳转到作者列表页
        return redirect('/author_list/')
       
    book_data = Book.objects.all()
    return render(request, 'add_author.html', {'book_list': book_data})


def delete_author(request):
    """删除作者"""
    # 1. 取到要删除作者的id
    delete_author_id = request.GET.get('id')
    age = request.GET.get('age')
    print(delete_author_id)
    print(age)
    # 2. 通过id找到数据，并删除
    Author.objects.filter(id=delete_author_id).delete()
    # 3. 让用户再访问作者列表页
    return redirect('/author_list/')


def edit_author(request):
    """编辑作者"""
    # 1. 取到要编辑的作者id值
    edit_author_id = request.GET.get('id')
    print(edit_author_id)
    # 2. 找到要编辑的作者对象
    edit_author_obj = Author.objects.get(id=edit_author_id)
    if request.method == "POST":
        # 3. 拿到编辑之后的数据
        new_author_name = request.POST.get('author_name')
        new_book_ids = request.POST.getlist('book_ids')
        # 4. 去数据库修改数据
        # 4.1 修改作者表
        edit_author_obj.name = new_author_name
        edit_author_obj.save()
        # 4.2 修改作者和书的关系表(set() 重新赋值)
        edit_author_obj.books.set(new_book_ids)
        # 5. 跳转到作者类表业
        return redirect('/author_list/')
    # 2.2 找到所有的书籍对象
    book_data = Book.objects.all()
    # 3. 返回一个页面
    return render(request, 'edit_author.html', {'author': edit_author_obj, 'book_list': book_data})


def upload(request):
    """上传文件"""
    if request.method == "POST":
        # 1. 取到用户发送的数据
        print(request.FILES)
        file_obj = request.FILES.get('file_name')
        print(file_obj.name)
        # 判断当前文件是否存在
        file_name = file_obj.name
        if os.path.exists(os.path.join(settings.BASE_DIR, file_name)):
            # 如果存在同名的文件
            name, suffix = file_name.split('.')
            name += '2'
            file_name = name + '.' + suffix
        # 从上文件对象里 一点一点读取数据，写到本地
        with open(file_name, 'wb') as f:
            # for line in file_obj:
            #     f.write(line)
            for chuck in file_obj.chunks():   # 官方推荐
                f.write(chuck)
    # 1. 第一次GET请求来给用户返回一个页面，让用户选择文件
    return render(request, 'upload.html')
