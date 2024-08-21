import PyPDF2
import ollama
import json
desired_model = "llama3.1:latest"


def extract_text_from_pdf(pdf_file: str) -> [str]:
    with open(pdf_file,'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf, strict = False)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)

        return pdf_text

extracted_text = extract_text_from_pdf("car_models_report.pdf")

text_to_process = "\n" .join(extracted_text)

ollama_client = ollama.Client()

prompt = f"""
The following is descriptive information about various car models. Extract and structure this information into JSON format. The JSON should include fields such as Car Model, Manufacturer, Year, Engine, Horsepower, Range, Top Speed, Price, and Description, please do not add any additional explanation and just generate the Json . Here's the text:
{text_to_process}

Respond with the JSON format of the extracted information.
"""
response = ollama_client.generate(model= desired_model, prompt=prompt)
print("Generated JSON:\n", response)

with open("car_models_2.json", "w") as json_file:
    json.dump(response, json_file, indent=4)

print("Json file saved as car_models.json")