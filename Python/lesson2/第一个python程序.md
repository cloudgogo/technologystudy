## 使用文本编辑器 
</div>
    <div class="x-wiki-content x-main-content"><p>在Python的交互式命令行写程序，好处是一下就能得到结果，坏处是没法保存，下次还想运行的时候，还得再敲一遍。</p>
<p>所以，实际开发的时候，我们总是使用一个文本编辑器来写代码，写完了，保存为一个文件，这样，程序就可以反复运行了。</p>
<p>现在，我们就把上次的<code>'hello, world'</code>程序用文本编辑器写出来，保存下来。</p>
<p>那么问题来了：文本编辑器到底哪家强？</p>
<h1>Visual Studio Code!</h1>
<p>我们推荐微软出品的<a href="https://code.visualstudio.com/" target="_blank">Visual Studio Code</a>，它不是那个大块头的Visual Studio，它是一个精简版的迷你Visual Studio，并且，Visual Studio Code可以跨！平！台！Windows、Mac和Linux通用。</p>
<p>请注意，<em>不要用Word和Windows自带的记事本</em>。Word保存的不是纯文本文件，而记事本会自作聪明地在文件开始的地方加上几个特殊字符（UTF-8 BOM），结果会导致程序运行出现莫名其妙的错误。</p>
<p>安装好文本编辑器后，输入以下代码：</p>
<pre><code class="php"><span class="keyword">print</span>(<span class="string">'hello, world'</span>)
</code></pre>
<p>注意<code>print</code>前面不要有任何空格。然后，选择一个目录，例如<code>C:\work</code>，把文件保存为<code>hello.py</code>，就可以打开命令行窗口，把当前目录切换到<code>hello.py</code>所在目录，就可以运行这个程序了：</p>
<pre><code class="undefined">C:\work&gt; python hello.py
hello, world
</code></pre>
<p>也可以保存为别的名字，比如<code>first.py</code>，但是必须要以<code>.py</code>结尾，其他的都不行。此外，文件名只能是英文字母、数字和下划线的组合。</p>
<p>如果当前目录下没有<code>hello.py</code>这个文件，运行<code>python hello.py</code>就会报错：</p>
<pre><code class="undefined">C:\Users\IEUser&gt; python hello.py
python: can't open file 'hello.py': [Errno 2] No such file or directory
</code></pre>
<p>报错的意思就是，无法打开<code>hello.py</code>这个文件，因为文件不存在。这个时候，就要检查一下当前目录下是否有这个文件了。如果<code>hello.py</code>存放在另外一个目录下，要首先用<code>cd</code>命令切换当前目录。</p>
<p>视频演示：</p>
<p><iframe src="//player.bilibili.com/player.html?aid=85858013" style="width:100%;height:480px" scrolling="no" border="0" frameborder="no" framespacing="0"></iframe></p>
<h3>直接运行py文件</h3>
<p>有同学问，能不能像.exe文件那样直接运行<code>.py</code>文件呢？在Windows上是不行的，但是，在Mac和Linux上是可以的，方法是在<code>.py</code>文件的第一行加上一个特殊的注释：</p>
<pre><code class="php"><span class="comment">#!/usr/bin/env python3</span>

<span class="keyword">print</span>(<span class="string">'hello, world'</span>)
</code></pre>
<p>然后，通过命令给<code>hello.py</code>以执行权限：</p>
<pre><code class="ruby"><span class="variable">$ </span>chmod a+x hello.py
</code></pre>
<p>就可以直接运行<code>hello.py</code>了，比如在Mac下运行：</p>
<p><img src="/files/attachments/923626376177344/0" data-src="/files/attachments/923626376177344/0" alt="run-python-in-shell"></p>
<h3>小结</h3>
<p>用文本编辑器写Python程序，然后保存为后缀为<code>.py</code>的文件，就可以用Python直接运行这个程序了。</p>
<p>Python的交互模式和直接运行<code>.py</code>文件有什么区别呢？</p>
<p>直接输入<code>python</code>进入交互模式，相当于启动了Python解释器，但是等待你一行一行地输入源代码，每输入一行就执行一行。</p>
<p>直接运行<code>.py</code>文件相当于启动了Python解释器，然后一次性把<code>.py</code>文件的源代码给执行了，你是没有机会以交互的方式输入源代码的。</p>
<p>用Python开发程序，完全可以一边在文本编辑器里写代码，一边开一个交互式命令窗口，在写代码的过程中，把部分代码粘到命令行去验证，事半功倍！前提是得有个27'的超大显示器！</p>
<h3>参考源码</h3>
<p><a href="https://github.com/michaelliao/learn-python3/blob/master/samples/basic/hello.py" target="_blank">hello.py</a></p>
</div><h3>读后有收获可以支付宝请作者喝咖啡，读后有疑问请加微信群讨论：</h3><p><img src="/files/attachments/1290305070432321/0"> <img src="/files/attachments/1283107913203778/0" <="" p=""></p><h3>还可以分享给朋友：</h3><p><a href="#0" onclick="shareToWeibo()" class="uk-button uk-button-danger"><i class="uk-icon-weibo"></i> 分享到微博</a></p>

## 
   