from django.utils.safestring import mark_safe       ###导入之后，才能使用page_str_list中的html标签

class Pagination():
    def __init__(self, request, queryset, page_limit = 7, subsection = 3, param_page='page'):
        """
        : 分页功能 : 
        : request  : 请求
        : queryset : 通过字典的内容进行数据库查询(元组)
        : page_limit : 每页显示的内容条目数量默认为7条
        : subsection : 显示当前页码的前后数量为默认4页，一共4*2+1=9页
        : param_page : 接收从前端 `name`属性 传来的数据再通过实例对象接收，来获取当前页 
        """
        page = request.GET.get(param_page,"1")  # 获取当前页
        if page.isdecimal():   # 判断用户传输过来的的字符串是否为数字
            page = int(page)   # 将字符串数字转换成整数
        else:
            page = 1           # 否则都等于1，第一页
        self.page = page                      # 当前页
        self.page_limit = page_limit          # 页面条目数量限制
        self.start = (page-1) * page_limit    # 计算起始页
        self.end   = page * page_limit        # 计算结束页
        self.one_page_queryset = queryset[self.start:self.end]         # 每页显示固定数量的内容; 数据库返回的 内容 进行分页|分段
        self.subsection = subsection
        #### 获取总条目数量
        entry_count = queryset.count()
        #### 计算分页总数
        page_count, div = divmod(entry_count, page_limit)
        if div:
            page_count += 1    # 如果有余数，则加一页
        self.page_count = page_count          # 总共需要的 多少页

    def page_num_html(self):

        #### 总页数，分段 subsection=4
        if self.page_count <= self.subsection * 2 + 1:  
            # 如果数据中条目没有超过页码的总数
            page_front = 1                 # 则页码从1开始
            page_behind = self.page_count  # 则页码从总条目数量结束
        else:  
             # 如果数据中条目 超过 页码的总数
             if self.page <= self.subsection:
                # 当当前页数小于等于页码小极值
                page_front = 1             # 则页码从1开始
                page_behind = self.subsection * 2 + 1  
             else:
                # 当当前页数小于等于页码大极值
                if (self.page + self.subsection) > self.page_count:
                    page_front = self.page_count - (self.subsection * 2 + 1)
                    page_behind = self.page_count
                else:
                    page_front = self.page - self.subsection 
                    page_behind = self.page + self.subsection 

        # 页码的HTML生成
        page_str_list = []  # 页码的HTML生成，放入到这里
        ## 计算前后页码，生成HTML代码
        for i in range(page_front, page_behind+1):   #### 总页数，分段，显示五页
            if i == self.page:    #### 当前页高亮显示
                element = f'<li class="page-item active"><a class="page-link" href="?page={i}">{i}</a></li>'  
            else:
                element = f'<li class="page-item"><a class="page-link" href="?page={i}">{i}</a></li>'
                
            page_str_list.append(element)
        # 标记page_str_list中的HTML格式的内容是安全的，不会被转换成字符串，而是HTML来生效
        page_str_list = mark_safe(''.join(page_str_list))    
        return page_str_list