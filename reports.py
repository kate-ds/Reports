from jinja2 import Template
import json


def open_rep(file_name='template.md'):
    with open(file_name,'r') as f:
        rep = f.readlines()
        return rep
    

def make_report(report, template_file="template.md", report_file="README.md"):
    """
    Function to save report to markdown file
    report: dict, 
    template_file: path to template
    report_file: path to markdown report, default README.md
    """
    template = open_rep(template_file)
    t = Template(''.join(template))
    readme_rendered = t.render(**report)

    with open(report_file,'w') as f:
        f.write(readme_rendered)
    return None


def read_dict_from_file(file_path):
    """
    Function to read the dictionary data from file
    file_path: str, json-file 
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return {}


def write_dict_to_file(data, file_path):
    """
    Function to write the dictionary data to file
    data: dict, data to write in file
    file_path: str, full path to file
    """
    with open(file_path, 'w') as file:
        json.dump(data, file)
