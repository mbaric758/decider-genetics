import ontoweaver
from biocypher import BioCypher

# Define the path to the mapping file. This time we define two paris of DATABASE:MAPPING_FILE mappings.
data_mappings = {f"./JOBIM_example/snv_subset_4.csv": f"./JOBIM_example/snv.yaml",
                 f"./JOBIM_example/treatments_subset.csv": f"./JOBIM_example/oncokb.yaml",
                 f"./JOBIM_example/cna_subset.csv": f"./JOBIM_example/cna.yaml"}

bc = BioCypher(biocypher_config_path = f"./JOBIM_example/biocypher_config.yaml",
               schema_config_path = f"./JOBIM_example/biocypher_schema.yaml")

# Extract nodes and edges from the mapping file. Reconciliate properties, and write nodes.
nodes, edges = ontoweaver.extract(filename_to_mapping=data_mappings, affix = "suffix")

fnodes, fedges = ontoweaver.fusion.reconciliate(nodes, edges, separator="|")

bc.write_nodes(fnodes)
bc.write_edges(fedges)

bc.write_schema_info(as_node=True)

data = bc.write_import_call()






