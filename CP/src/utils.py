def dataprep():
    ds_path = "VLSI-optimization\dataset\instances\instances"
    instances = os.listdir(ds_path)
    for instance in instances:
        instance_path = os.path.join(ds_path, instance)
        print(instance_path)