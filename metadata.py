def yum(metadata):
    if node.has_bundle('yum'):
        metadata.setdefault('yum', {})
        metadata['yum'].setdefault('extra_packages', [])
        for package in ['java-1.8.0-openjdk-headless']:
            if package not in metadata['yum']['extra_packages']:
                metadata['yum']['extra_packages'].append(package)
        
    return metadata
