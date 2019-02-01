![screenshot from 2019-02-01 14-57-42](https://user-images.githubusercontent.com/35887568/52141645-5bd50c80-267c-11e9-910c-0da4ed83b1df.png)
![screenshot from 2019-02-01 14-57-49](https://user-images.githubusercontent.com/35887568/52141647-5e376680-267c-11e9-9bdb-f52b75963f0e.png)
![screenshot from 2019-02-01 14-57-57](https://user-images.githubusercontent.com/35887568/52141653-64c5de00-267c-11e9-8764-7d21d7b29717.png)
![screenshot from 2019-02-01 14-57-59](https://user-images.githubusercontent.com/35887568/52141657-68596500-267c-11e9-8583-0f1c8e692b81.png)

1) Download & link language model of Spacy for the english language
```
>>> pip install rasa_nlu
>>> pip install rasa_core
```
```
2) For better result we can use large model: 
>>> python -m spacy download en_core_web_lg
```
3) Linking manually:
```
python -m spacy link en_core_web_lg en
```


4) ###Train

#####train nlu
```bash
python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project default
```

5) #####train core
```bash
python -m rasa_core.train -d domain.yml -s stories.md -c policy_config.yml -o models/dialogue
```

6) ####Interactive training
```bash
python -m rasa_core.train interactive -o models/dialogue -d domain.yml -s stories.md --nlu models/default/nlu --endpoints endpoints.yml --config policy_config.yml
```




7) ######Main Functionality for testing########
######Run################

#####rasa core nlu tracker
#####actions
```bash
python -m rasa_core_sdk.endpoint --actions actions --port 8000
```

```bash
python run_all.py
```
###chatbot
```
yarn install
yarn build
yarn serve
```
