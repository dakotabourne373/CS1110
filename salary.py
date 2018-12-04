#Dakota Bourne db2nb
"""
This program is designed to take and parse data on a salary website, using a name that is given to a report function.
"""
import urllib.request, re

job_finder = re.compile(r'(Job title:)(.+)[<]')
salary_finder = re.compile(r'(paytype.amount,) (\d+.\d)')
rank_finder = re.compile(r'(University of Virginia rank)\S+(\d)')


def report(name):
    """
    report takes a name, makes it suitable for URL, applies it and opens the URL and parse the data for the person's Job
    Title, Salary, and rank within the school system
    """
    job_title = 'None'
    salary = 0
    rank = 0
    if ' ' in name and ',' not in name:
        name = name.lower()
        name = name.split(' ')
        name = '-'.join(name)
    elif ',' in name:
        normal_lst = []
        name = name.lower().replace(' ', '')
        name = name.split(',')
        for i in range(0, len(name)):
            normal_lst.append(name[-i + 1])
        name = '-'.join(normal_lst)
    try:
        file = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/uva2016/' + name)
    except:
        return job_title, salary, rank
    for line in file:
        x = line.decode('utf-8')
        if '<meta property="og:description" content="Job title' in x:
            for match in job_finder.finditer(x):
                job_title = match.group(2)
                if '&amp;' in job_title:
                    job_title = job_title.replace('&amp;', '&')
                if '&lt;' in job_title:
                    job_title = job_title.replace('&lt;', '<')
                if '&gt;' in job_title:
                    job_title = job_title.replace('&gt;', '>')
        if 'paytype.amount' in x:
            for match in salary_finder.finditer(x):
                salary = float(match.group(2))
        if 'University of Virginia rank' in x:
            for match in rank_finder.finditer(x):
                rank = int(match.group(2))
    return job_title.strip(), salary, rank
