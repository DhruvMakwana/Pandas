Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
# (Q) How to install Pandas?
</br>The best way to get pandas is via conda
</br></br>`conda install pandas`
</br>You can also install pandas using pip command
</br></br>`pip install pandas`
## (Q)What problem does pandas solve?
Python has long been great for data munging and preparation, but less so for data analysis and modeling. pandas helps fill this gap, enabling you to carry out your entire data analysis workflow in Python without having to switch to a more domain specific language like R.

Combined with the excellent IPython toolkit and other libraries, the environment for doing data analysis in Python excels in performance, productivity, and the ability to collaborate.

pandas does not implement significant modeling functionality outside of linear and panel regression; for this, look to statsmodels and scikit-learn. More work is still needed to make Python a first class statistical modeling environment, but we are well on our way toward that goal.

### Library Highlights
*	A fast and efficient DataFrame object for data manipulation with integrated indexing;
*	Tools for reading and writing data between in-memory data structures and different formats: CSV and text files, Microsoft Excel, SQL databases, and the fast HDF5 format;
*	Intelligent data alignment and integrated handling of missing data: gain automatic label-based alignment in computations and easily manipulate messy data into an orderly form;
*	Flexible reshaping and pivoting of data sets;
*	Intelligent label-based slicing, fancy indexing, and subsetting of large data sets;
*	Columns can be inserted and deleted from data structures for size mutability;
*	Aggregating or transforming data with a powerful group by engine allowing split-apply-combine operations on data sets;
*	High performance merging and joining of data sets;
*	Hierarchical axis indexing provides an intuitive way of working with high-dimensional data in a lower-dimensional data structure;
*	Time series-functionality: date range generation and frequency conversion, moving window statistics, moving window linear regressions, date shifting and lagging. Even create domain-specific time offsets and join time series without losing data;
*	Highly optimized for performance, with critical code paths written in Cythonor C.
*	Python with pandas is in use in a wide variety of academic and commercialdomains, including Finance, Neuroscience, Economics, Statistics, Advertising, Web Analytics, and more.
</br></br></br>For Visual representation of pandas visit here(https://jalammar.github.io/gentle-visual-intro-to-data-analysis-python-pandas/)

## Reference:
### Community tutorials
This is a guide to many pandas tutorials by the community, geared mainly for new users.

### pandas cookbook by Julia Evans
The goal of this 2015 cookbook (by <a href="https://jvns.ca/">Julia Evans</a>) is to give you some concrete examples for getting started with pandas. These are examples with real-world data, and all the bugs and weirdness that entails. For the table of contents, see the <a href="https://github.com/jvns/pandas-cookbook">pandas-cookbook GitHub repository</a>.

### Learn pandas by Hernan Rojas
A set of lesson for new pandas users: https://bitbucket.org/hrojas/learn-pandas

### Practical data analysis with Python
This <a href="https://wavedatalab.github.io/datawithpython">guide</a> is an introduction to the data analysis process using the Python data ecosystem and an interesting open dataset. There are four sections covering selected topics as <a href="https://wavedatalab.github.io/datawithpython/munge.html">munging data</a>, <a href="https://wavedatalab.github.io/datawithpython/aggregate.html">aggregating data</a>, <a href="https://wavedatalab.github.io/datawithpython/visualize.html">visualizing data</a> and <a href="https://wavedatalab.github.io/datawithpython/timeseries.html">time series</a>.

### Exercises for new users
Practice your skills with real data sets and exercises. For more resources, please visit the main <a href="https://github.com/guipsamora/pandas_exercises">repository.</a>

### Modern pandas
Tutorial series written in 2016 by <a href="https://github.com/TomAugspurger">Tom Augspurger</a>. The source may be found in the GitHub repository <a href="https://github.com/TomAugspurger/effective-pandas">TomAugspurger/effective-pandas.</a>

* <a href="https://tomaugspurger.github.io/modern-1-intro.html">Modern Pandas</a>
* <a href="https://tomaugspurger.github.io/method-chaining.html">Method Chaining</a>
* <a href="https://tomaugspurger.github.io/modern-3-indexes.html">Indexes</a>
* <a href="https://tomaugspurger.github.io/modern-3-indexes.html">Performance</a>
* <a href="https://tomaugspurger.github.io/modern-5-tidy.html">Tidy Data</a>
* <a href="https://tomaugspurger.github.io/modern-6-visualization.html">Visualization</a>
* <a href="https://tomaugspurger.github.io/modern-6-visualization.html">Timeseries</a>

### Excel charts with pandas, vincent and xlsxwriter
<a href="https://pandas-xlsxwriter-charts.readthedocs.io/">Using Pandas and XlsxWriter to create Excel charts</a>

### Video tutorials
<a href="https://www.youtube.com/watch?v=5JnMutdy6Fw">Pandas From The Ground Up</a> (2015) (2:24) <a href="https://github.com/brandon-rhodes/pycon-pandas-tutorial">GitHub repo</a><br>
<a href="https://www.youtube.com/watch?v=-NR-ynQg0YM">Introduction Into Pandas</a> (2016) (1:28) <a href="https://github.com/chendaniely/2016-pydata-carolinas-pandas">GitHub repo</a><br>
<a href="https://www.youtube.com/watch?v=7vuO9QXDN50">Pandas: .head() to .tail()</a> (2016) (1:26) <a href="https://github.com/TomAugspurger/pydata-chi-h2t">GitHub repo</a><br>
<a href="https://www.youtube.com/playlist?list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y">Data analysis in Python with pandas</a> (2016-2018) <a href="https://github.com/justmarkham/pandas-videos">GitHub repo</a> and <a href="https://nbviewer.jupyter.org/github/justmarkham/pandas-videos/blob/master/pandas.ipynb">Jupyter Notebook</a><br>
<a href="https://www.youtube.com/playlist?list=PL5-da3qGB5IBITZj_dYSFqnd_15JgqwA6">Best practices with pandas</a> (2018) <a href="https://github.com/justmarkham/pycon-2018-tutorial">GitHub repo</a> and <a href="https://nbviewer.jupyter.org/github/justmarkham/pycon-2018-tutorial/blob/master/tutorial.ipynb">Jupyter Notebook</a><br>

### Various tutorials
<a href="https://wesmckinney.com/archives.html">Wes McKinney’s (pandas BDFL) blog</a><br>
<a href="http://www.randalolson.com/2012/08/06/statistical-analysis-made-easy-in-python/">Statistical analysis made easy in Python with SciPy and pandas DataFrames, by Randal Olson</a><br>
<a href="https://conference.scipy.org/scipy2013/tutorial_detail.php?id=109">Statistical Data Analysis in Python, tutorial videos, by Christopher Fonnesbeck from SciPy 2013</a><br>
<a href="https://nbviewer.ipython.org/github/twiecki/financial-analysis-python-tutorial/blob/master/1.%20Pandas%20Basics.ipynb">Financial analysis in Python, by Thomas Wiecki</a><br>
<a href="http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/">Intro to pandas data structures, by Greg Reda</a><br>
<a href="https://manishamde.github.io/blog/2013/03/07/pandas-and-python-top-10/">Pandas and Python: Top 10, by Manish Amde</a><br>
<a href="https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python">Pandas DataFrames Tutorial, by Karlijn Willems</a><br>
<a href="https://tutswiki.com/pandas-cookbook/chapter1/">A concise tutorial with real life examples</a><br>
