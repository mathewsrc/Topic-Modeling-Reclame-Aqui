# Topic Modeling Reclame Aqui

## Course Completion Work presented to obtain the title of specialist in Data Science and Analytics – 2023

## **Title: Comparison of Topic Modeling Approaches on Complaints Related to the E-Commerce Industry**

### Abstract

  The electronics sector faces a great challenge in dealing with a large volume of consumer complaints, which can have various origins, from issues such as delivery time to problems with service cancellations. These complaints can negatively impact a company's reputation and affect its ability to retain and attract new customers. Topic modeling becomes fundamental in this context because it can help companies better understand and categorize consumer complaints in an automated way. In this context, this project aimed to compare and evaluate the performance of three popular topic modeling algorithms: LDA, BERTopic, and LSI, in extracting topics from customer complaints on the Brazilian website "Reclame Aqui" and identifying relevant topics. The project used a dataset of approximately twelve thousand customer complaints related to products and services from the major e-commerce platforms in Brazil. The data was preprocessed and used in training and optimizing topic modeling models, and the performance was evaluated based on the average coherence value. The evaluation results showed that the LDA and BERTopic models were able to extract informative topics from the data. In terms of score, BERTopic had the best performance among the models using the average coherence value as a comparison metric. The findings of this project suggest that companies seeking to obtain valuable information related to customer complaints can benefit from the use of topic modeling algorithms, such as LDA and BERTopic, to better understand their customers' concerns and take data-driven actions to improve customer satisfaction.

Keywords: Transformers; Latent Dirichlet Allocation; Latent Semantic Indexing; BERTopic; Latent Semantic Indexing

### Overview

![image](https://github.com/mathewsrc/Topic-Modeling-Reclame-Aqui/assets/94936606/f8be9504-df7d-45a0-bb7f-858cec1188cf)

### Project structure

### Results

LDA - Intertopic Distance map 

<img src="https://github.com/mathewsrc/Topic-Modeling-Reclame-Aqui/assets/94936606/1dcf89e7-2013-470f-90b9-4f323f08aeae" width=50% height=50%>

LDA - Terms relevance in each topic

<img src="https://github.com/mathewsrc/Topic-Modeling-Reclame-Aqui/assets/94936606/4b966821-f399-4aa3-80fc-1243fb6a068f" width=50% height=50%>

BERTopic - Intertopic Distance map

<img src="https://github.com/mathewsrc/Topic-Modeling-Reclame-Aqui/assets/94936606/b8cdef99-385a-447d-98a2-2407a8d3b23b" width=50% height=50%>

BERTopic - Intertopic Distance map

<img src="https://github.com/mathewsrc/Topic-Modeling-Reclame-Aqui/assets/94936606/5d1af046-fe10-4b7c-a0fd-9a8aba2072ab" width=50% height=50%>

Models comparison (LSI, LDA, and BERTopic) using coherence measure

<img src="https://github.com/mathewsrc/Topic-Modeling-Reclame-Aqui/assets/94936606/9e6d314d-1e7d-4eba-867b-146b51bd78de" width=50% height=50%>

### Conclusion

  In conclusion, the present project revealed that topic modeling is a highly effective technique for extracting structured information from large customer complaints data sets. Notably, the BERTopic and LDA models were able to identify the main reasons underlying complaints related to e-commerce in Brazil, highlighting, with relevance, themes relating to problems with credit cards, payments, delays in deliveries, delivery times, and returns, as well as problems arising from direct service with companies.
  On the other hand, the LSI model demonstrated limitations in separating complaints into topics with precise themes. The analysis of the terms of the generated topics indicated the overlap of many terms, such as "store", "value" and "deadline", in different topics, which suggests the need for further investigation.
  The results obtained indicate that, by identifying the most common concerns and problems among customers, companies can better understand the reasons underlying customer dissatisfaction and take effective measures to improve their products or services, which, in turn, can lead to better customer relationships and satisfaction.
  Furthermore, the findings of this study highlight that topic modeling can help companies deal more effectively with customer complaints, balancing the impact on their market value and reputation, and promoting data-driven decision-making to reduce customer attrition and therefore improve the customer experience.
  In summary, it is expected that the contributions of this study can serve as a basis for the development of future research in the area of ​​topic modeling applied to consumer feedback and for the development of practical solutions that can be used by companies interested in improving the experience of its consumers and that can contribute to future work involving topic modeling in different areas of interest. The LDA and BERTopic models proved to be models with excellent performance in extracting thematic terms from complaints, opening a path of opportunities for new applications. BERTopic offers a wide range of uses such as topic evolution analysis over time and incremental topic modeling, which were not explored in this project and which could bring even better results in understanding the problems present in complaints.
