import spacy
nlp = spacy.load('en_core_sci_lg')

text = "Our school is in dire need of an extension to accommodate the growing number of students and provide them with" \
       " the best possible learning environment. With this expansion, we can provide students with additional classrooms," \
       " state-of-the-art technology, and modern facilities that will enhance their educational experience and" \
       " support their academic success. Our school has been a cornerstone of our community for many years, and " \
       "it's time for us to invest in its future. The expansion of our building will not only improve the quality " \
       "of education for our students, but it will also create a safer and more comfortable learning environment." \
       " We need your support to make this dream a reality. With your donation, we can bring this project to life and " \
       "create a brighter future for our students. Every contribution, big or small, can make a difference in the " \
       "lives of our students and the future of our school. Join us in our mission to give our students the best " \
       "education possible. Donate now and help us build a brighter future for our school!"

doc = nlp(text)

print(doc.ents)
