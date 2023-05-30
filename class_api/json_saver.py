import codecs
import json

from class_api.class_api import Vacancy


class JSONSaver:
    pass

    def clear_json(self):
        with open("vacancy.json", "w") as f:
            json.dump([], f, indent=2, ensure_ascii=False)

    def add_vacancy_hh(self, vacancy):
        self.clear_json()

        for item in vacancy:

            vacancy = Vacancy(item['name'], item['url'], item['salary'], item['snippet']['requirement'])

            text_json = {
                "name": vacancy.name,
                "url": vacancy.url,
                "salary": vacancy.salary,
                "conditions": vacancy.conditions
            }

            with codecs.open('vacancy.json', 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                data.append(text_json)

            with codecs.open('vacancy.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

    def add_vacancy_superjob(self, vacancy):
        for item in vacancy:
            vacancy = Vacancy(item['profession'], item['link'], item['payment_from'], item['candidat'])

            text_json = {
                "name": vacancy.name,
                "url": vacancy.url,
                "salary": vacancy.salary,
                "conditions": vacancy.conditions
            }

            with codecs.open('vacancy.json', 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                data.append(text_json)

            with codecs.open('vacancy.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

    def data_filter(self, filter_words):
        with codecs.open('vacancy.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            list_vacancies = []
            for v in data:
                if any(item in v['conditions'] for item in filter_words.split()):
                    list_vacancies.append(v)

        return list_vacancies
