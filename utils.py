from django.conf import settings
from openai import OpenAI

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_sql_query(prompt):
    # if prompt:

        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert SQL query generator. can you always return the column names at the top of the table You have all the information for this table: ('id', 'int', 'NO', 'PRI', NULL, 'auto_increment'), ('name', 'varchar(100)', 'NO', '', NULL, ''), ('phone', 'varchar(20)', 'YES', '', NULL, ''), ('email', 'varchar(100)', 'YES', '', NULL, ''), ('address', 'varchar(255)', 'YES', '', NULL, ''), ('created_at', 'timestamp', 'YES', '', 'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED'), number_of_windows, price. You are only to query information or generate SQL prompts based on the problem. remember to only give the sql statement or else an error will occur. also infer by what i mean. If i say order by name, i mean the name of each person.in the customers tables there are id, name, phone, email, address, created_at  when i ask for first inital of something, only giev the first letter, for ex. first inital of last name would be the foirst letter, fix the time stamp:exafter 10 am means on any givven day The error " '10:00:00'" occurs because MySQL expects a full datetime value (YYYY-MM-DD HH:MM:SS) for a TIMESTAMP column but is receiving only a time (HH:MM:SS)., if there is no other time stmap information, it doesn't matter jusThe Prompt is:"}
    ,
            {"role": "user", "content": prompt}
        ],
        temperature=0)
        return response.choices[0].message.content
    # else:
    #     response = client.chat.completions.create(model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "system", "content": "You are an expert SQL query generator. You have all the information for this table: ('id', 'int', 'NO', 'PRI', NULL, 'auto_increment'), ('name', 'varchar(100)', 'NO', '', NULL, ''), ('phone', 'varchar(20)', 'YES', '', NULL, ''), ('email', 'varchar(100)', 'YES', '', NULL, ''), ('address', 'varchar(255)', 'YES', '', NULL, ''), ('created_at', 'timestamp', 'YES', '', 'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED'). You are only to query information or generate SQL prompts based on the problem. remember to only give the sql statement or else an error will occur. also infer by what i mean. If i say order by name, i mean the name of each person.in the customers tables there are id, name, phone, email, address, created_at The Prompt is:"}
    # ,
    #         {"role": "user", "content": preset_idea}
    #     ],
    #     temperature=0)
    #     return response.choices[0].message.content
