# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return f"{self.name}({self.age})"

# p = person('nagendra', 36)
# print(p)
# print(p.name)
# print(p.age)

from dataclasses import dataclass       
from pathlib import Path
# creating entity 
@dataclass(frozen=True)
def dataingetionconfig():
    root_dir = Path
    source_url = str
    local_dir_path = Path
    unzip_dir = str

class ConfigureMAnager:
    def __init__(
            self,
            config_filepath = path1,
            params_filepath = path2,
            schema_filepath = path3):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directory(self.config.data_ingestion)

    def get_data_ingetion_configue(self) -> dataingetionconfig:
        config = self.config.data_ingetion

        create_directory(config.root_dir)

        data_ingetion_configue = dataingetionconfig(
            root_dir = config.root_dir,
        )

        return get_data_ingetion_configue
        
