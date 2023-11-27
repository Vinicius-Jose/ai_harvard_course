import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    links = corpus.get(page)
    result = {key:0 for key in corpus.keys()}
    len_result =len(result)
    if not links:
        for key in result.keys():
            result[key] = 1/len_result
    else:
        random_prob = (1 - damping_factor) / len_result
        for p in links:
            result[p] = (1/len(links) * damping_factor) 
        result = {key:value + random_prob for key, value in result.items()}
    return result


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page = random.choice(list(corpus.keys()))
    result = {key:0 for key in corpus.keys()}
    for _ in range(n):
        result[page] += 1
        model = transition_model(corpus,page,damping_factor)
        max_prob = 0
        random_page = random.random()
        for key,value in model.items():
            max_prob += value
            if random_page <=  max_prob:
                page = key
                break
        
    sum_result = sum(list(result.values()))
    for key,value in result.items():
            result[key] = value/sum_result

    return result


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    len_corpus = len(corpus)
    result = {key:1/len_corpus for key in corpus.keys()}
    
    accuracy = 0.001
    choose_random = (1-damping_factor)/ len_corpus

    while True:
        estimated_pages = 0
        for key,_ in corpus.items():
            sum_val = 0
            for i  in corpus:
                if key in corpus[i]:
                    sum_val +=  result[i] / len(corpus[i])
            formula = choose_random + (damping_factor * sum_val)
            
            if abs(result[key]  - formula) < accuracy :
                estimated_pages += 1
            result[key] = formula
        if estimated_pages >= len(result):
            sum_result = sum(list(result.values()))
            for key,value in result.items():
                result[key] = value/sum_result
            return result
            




if __name__ == "__main__":
    main()
