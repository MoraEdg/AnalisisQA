import matplotlib.pyplot as plt
import pandas as pd

# Datos del archivo attribute-details.csv
attribute_details_data = {
    "Category": ["Package, Class, Method", "Package, Class, Method", "Package, Class, Method", "Package, Class, Method", "Package, Class",
                 "Package, Class", "Class", "Class", "Class", "Class", "Project", "Class", "Class", "Class", "Class", "Class", "Class",
                 "Class", "Class", "Class", "Package", "Package", "Package", "Package", "Package", "Class", "Class", "Project", "Project",
                 "Project", "Project", "Class", "Class", "Package", "Package", "Class", "Class", "Package", "Package", "Class", "Class",
                 "Method", "Method", "Method", "Method", "Method", "Method", "Method", "Method", "Method", "Method", "Method", "Method", "Method"][:47],
    "Code": ["Coupling", "Lack of Cohesion", "Complexity", "Size", "LOC", "WMC", "DIT", "NOC", "CBO", "CBO_LIB", "CBO_APP", "RFC", "SRFC",
             "LCOM", "LCAM", "NOF", "NOM", "NOSF", "NOSM", "SI", "CMLOC", "EC", "AC", "#(C&I)", "#I", "#C", "NORM", "C3", "nofP", "nofPa",
             "nofEE", "NoPC", "NoHPC", "LTCC", "ATFD", "Ins", "Abs", "ND", "InDegree", "OutDegree", "Degree", "MCC", "NBD", "LOC.2", "#Pa",
             "#MC", "#AF"][:47],
    "Description": ["Measures coupling value between two classes A and B.", "Measure how well the methods of a class are related to each other.",
                    "Implies being difficult to understand and describes the interactions between a number of entities.",
                    "Measured by the number of lines or methods in the code.", "The number of all nonempty, non-commented lines of the body of the class.",
                    "The weighted sum of all class’ methods an represents the McCabe complexity of a class.", "The position of the class in the inheritance tree.",
                    "The number of direct subclasses of a class.", "The number of classes that a class is coupled to.", "The number of dependent library classes.",
                    "The number of dependent classes in the application.", "The number of the methods that can be potentially invoked in response to a public message received by an object of a particular class.",
                    "The number of the methods that can be potentially invoked in simple response to a public message received by an object of a particular class.",
                    "Measure how methods of a class are related to each other.", "CAM metric is the measure of cohesion based on parameter types of methods. LCAM = 1-CAM",
                    "The number of fields (attributes) in a class", "The number of methods in a class.", "The number of static fields in a class.",
                    "The number of static methods in a class.", "Measures the extent to which subclasses override their ancestors classes.",
                    "Total number of all nonempty, non-commented lines of methods inside a class.", "Outgoing Coupling. The number of classes in other packages that the classes in the package depend upon is an indicator of the package's dependence on externalities.",
                    "Incoming Coupling. The number of classes in other packages that depend upon classes within the package is an indicator of the package's responsibility.",
                    "Total number of Classes & Interfaces.", "Total number of Interfaces.", "Total number of classes.", "The number of Overridden Methods.",
                    "The max value of Coupling, Cohesion, Complexity metrics", "Number of Packages in the project", "Number of External Packages referenced by the project",
                    "Number of External classes and interfaces referenced by the project", "Number of classes with high coupling, high complexity or low cohesion in the project",
                    "Number of classes with high coupling, high complexity and low cohesion in the project", "Measures the lack cohesion between the public methods of a class.",
                    "The number of classes whose attributes are directly or indirectly reachable from the investigated class.", "Measure the relative susceptibility of class to changes.",
                    "Measure the degree of abstraction of the package.", "Normalized Distance metric is used to measure the balance between stability and abstractness.",
                    "In-degree of corresponding graph vertex of the class", "Out-degree of corresponding graph vertex of the class", "Degree of corresponding graph vertex of the class",
                    "McCabe Cyclomatic Complexity", "Nested Block Depth", "Method Lines of Code", "Number of Parameters", "Number of Methods  Called",
                    "Number of Accessed Fields"][:47]
}

# Crear un DataFrame para los datos
attribute_details_df = pd.DataFrame(attribute_details_data)

# Datos del archivo repositories.csv
repositories_data = {
    "Repository name": ["Spring framework", "Junit-5", "Apache kafka", "Apache lucene-solr", "Dropwizard", "Checkstyle", "Hadoop", "Selenium", "Skywalking", "Signal android"],
    "Commits": [22208, 6621, 8590, 34789, 5702, 9922, 24612, 26532, 6242, 7015],
    "Watches": [3500, 269, 1100, 332, 426, 218, 1000, 1300, 839, 946],
    "Stars": [41400, 4400, 18000, 4100, 7900, 5800, 11300, 19800, 16100, 19800],
    "Forks": [28800, 991, 9600, 2700, 3300, 7700, 7000, 6200, 4700, 4700]
}

# Crear un DataFrame para los datos
repositories_df = pd.DataFrame(repositories_data)

# Gráfico de barras para Commits por Repositorio
plt.figure(figsize=(10, 6))
plt.bar(repositories_df["Repository name"], repositories_df["Commits"], color='skyblue')
plt.xlabel('Repository')
plt.ylabel('Commits')
plt.title('Commits per Repository')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Gráfico de dispersión para Stars vs Forks por Repositorio
plt.figure(figsize=(10, 6))
plt.scatter(repositories_df["Stars"], repositories_df["Forks"], color='orange', s=repositories_df["Watches"]/10)
plt.xlabel('Stars')
plt.ylabel('Forks')
plt.title('Stars vs Forks per Repository')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Gráfico de barras para Description de atributos
plt.figure(figsize=(10, 6))
plt.bar(attribute_details_df["Description"], attribute_details_df["Category"].apply(lambda x: x.count(',') + 1), color='lightgreen')
plt.xlabel('Attribute Description')
plt.ylabel('Count')
plt.title('Count of Attributes by Description')
plt.xticks(rotation=90, ha='right')
plt.tight_layout()
plt.show()
