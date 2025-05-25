import json
import pandas as pd

def create_sample_dataset():
    """Create a sample dataset for testing when the full ArXiv dataset is not available"""
    
    sample_papers = [
        {
            "id": "1706.03762",
            "title": "Attention Is All You Need",
            "authors": "Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin",
            "categories": "cs.CL,cs.AI",
            "abstract": "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely."
        },
        {
            "id": "1512.03385",
            "title": "Deep Residual Learning for Image Recognition",
            "authors": "Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun",
            "categories": "cs.CV",
            "abstract": "Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously. We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions."
        },
        {
            "id": "1406.2661",
            "title": "Generative Adversarial Networks",
            "authors": "Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, Yoshua Bengio",
            "categories": "stat.ML,cs.LG",
            "abstract": "We propose a new framework for estimating generative models via an adversarial process, in which we simultaneously train two models: a generative model G that captures the data distribution, and a discriminative model D that estimates the probability that a sample came from the training data rather than G."
        },
        {
            "id": "1810.04805",
            "title": "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
            "authors": "Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova",
            "categories": "cs.CL",
            "abstract": "We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers. Unlike recent language representation models, BERT is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers."
        },
        {
            "id": "2005.14165",
            "title": "Language Models are Few-Shot Learners",
            "authors": "Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei",
            "categories": "cs.CL",
            "abstract": "Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a specific task. While typically task-agnostic in architecture, this method still requires task-specific fine-tuning datasets of thousands or tens of thousands of examples. By contrast, humans can generally perform a new language task from only a few examples or from simple instructions."
        },
        {
            "id": "1807.03748",
            "title": "Graph Convolutional Networks for Text Classification",
            "authors": "Liang Yao, Chengsheng Mao, Yuan Luo",
            "categories": "cs.CL,cs.AI",
            "abstract": "Text classification is an important and classical problem in natural language processing. There have been a number of studies that applied convolutional neural networks (convolution on regular grid, e.g., sequence) to classification. However, only a limited number of studies have explored the more flexible graph convolutional neural networks (convolution on non-Euclidean domain) for the task."
        },
        {
            "id": "1503.02531",
            "title": "Distilling the Knowledge in a Neural Network",
            "authors": "Geoffrey Hinton, Oriol Vinyals, Jeff Dean",
            "categories": "stat.ML,cs.LG,cs.NE",
            "abstract": "A very simple way to improve the performance of almost any machine learning algorithm is to train many different models on the same data and then to average their predictions. Unfortunately, making predictions using a whole ensemble of models is cumbersome and may be too computationally expensive to allow deployment to a large number of users."
        },
        {
            "id": "1412.3555",
            "title": "Conditional Generative Adversarial Nets",
            "authors": "Mehdi Mirza, Simon Osindero",
            "categories": "cs.LG,cs.AI,stat.ML",
            "abstract": "Generative Adversarial Nets were recently introduced as a novel way to train generative models. In this work we introduce the conditional version of generative adversarial nets, which can be constructed by simply feeding the data, y, we wish to condition on to both the generator and discriminator."
        },
        {
            "id": "1409.1556",
            "title": "Very Deep Convolutional Networks for Large-Scale Image Recognition",
            "authors": "Karen Simonyan, Andrew Zisserman",
            "categories": "cs.CV",
            "abstract": "In this work we investigate the effect of the convolutional network depth on its accuracy in the large-scale image recognition setting. Our main contribution is a thorough evaluation of networks of increasing depth using an architecture with very small (3x3) convolution filters, which shows that a significant improvement on the prior-art configurations can be achieved by pushing the depth to 16-19 weight layers."
        },
        {
            "id": "1611.07004",
            "title": "Language Modeling with Gated Convolutional Networks",
            "authors": "Yann N. Dauphin, Angela Fan, Michael Auli, David Grangier",
            "categories": "cs.CL",
            "abstract": "The prevalent approach to sequence to sequence learning maps an input sequence to a variable length output sequence via recurrent neural networks (RNNs). We introduce an architecture based on convolutional neural networks (CNNs) for both encoding and decoding which is parallelizable and reaches new state of the art in speed and accuracy for neural machine translation."
        }
    ]
    
    # Save as JSONL file (one JSON object per line)
    with open('sample_arxiv_data.json', 'w') as f:
        for paper in sample_papers:
            f.write(json.dumps(paper) + '\n')
    
    print("Sample dataset created: sample_arxiv_data.json")
    print(f"Contains {len(sample_papers)} sample papers")
    return 'sample_arxiv_data.json'

if __name__ == "__main__":
    create_sample_dataset()