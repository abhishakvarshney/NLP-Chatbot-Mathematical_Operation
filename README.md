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