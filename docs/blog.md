---
layout: page
title: blog
permalink: /blog
---

# 记录一下使用github搭建博客的注意事项

首先按照[教程](https://docs.github.com/en/pages/quickstart)指导，可以轻松地搭建起一个简单的静态网页，
但是存在几个问题：

1.怎么定制字体等样式？
2.怎么做一个导航栏出来？


通过配置front matter在某个页面定制jellyii：
在页首添加以下文本：
---
layout: page
title: my test
permalink: /test
---
参考https://jekyllrb.com/docs/front-matter/
这里的配置会覆盖`_config.yml`中的配置。

