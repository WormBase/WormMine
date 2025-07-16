# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

WormMine is an InterMine-based data warehouse for nematode genomics, primarily focused on C. elegans and related species. It integrates diverse biological data sources including genomic annotations, protein sequences, ontologies, and experimental data from WormBase and other databases.

## Build System and Common Commands

### Core Build Commands
```bash
# Build the database model
./gradlew dbmodel:buildDB

# Clean and rebuild everything
./gradlew clean buildDB

# Build and deploy the webapp
./gradlew webapp:war
./gradlew webapp:cargoDeployRemote

# Run the webapp locally
./gradlew webapp:gretty

# Run post-processing steps
./gradlew dbmodel:postprocess
```

### Data Processing Commands
```bash
# Download all external data sources
./support/scripts/get/get_all.sh

# Deploy and preprocess data
./support/scripts/deploy/deploy.sh

# Run post-processing Python scripts
cd support/scripts/post_processing
python remove_genes.py
python edit_protein.py
```

### Test and Verification
```bash
# Run integration tests (if available)
./gradlew test

# Check database status
./support/scripts/testing/testing.py
```

## Project Architecture

### Multi-Module Structure
- **`dbmodel/`**: Database model generation and data integration
- **`webapp/`**: Web application and user interface
- **`support/`**: Data processing scripts and configuration

### Data Integration Pipeline
1. **Data Acquisition**: External data downloaded via `support/scripts/get/` scripts
2. **Preprocessing**: Raw data converted via `support/scripts/deploy/deploy.sh`
3. **Integration**: InterMine build process loads data using `project.xml` source definitions
4. **Post-processing**: Database cleanup via Python scripts in `support/scripts/post_processing/`
5. **Webapp Deployment**: War file creation and Tomcat deployment

### Key Configuration Files
- **`project.xml`**: Defines all data sources, integration settings, and post-processing steps
- **`wormmine.properties`**: Database connections, webapp settings, OAuth configuration
- **`gradle.properties`**: InterMine version dependencies
- **`support/properties_xpath/`**: XPath mapping files for XML-to-object conversion

### Bio-Sources Architecture
Data sources are configured in `project.xml` with multiple types:
- **wormbase-acedb**: WormBase AceDB XML data (genes, proteins, variations, etc.)
- **fasta**: Sequence data (genomic, transcript, CDS, protein)
- **gff**: Genomic annotations
- **ontology sources**: GO, anatomy, disease ontologies
- **external integrations**: Panther, UniProt, InterPro

### Post-Processing Scripts
Located in `support/scripts/post_processing/` using Poetry dependency management:
- **Gene processing**: Remove specific genes, update annotations
- **Protein processing**: Clean protein data, remove obsolete entries  
- **Anatomy processing**: Update anatomy term mappings
- **HGNC integration**: Add human gene name cross-references

## Data Management

### Species Support
Primary focus on C. elegans (taxon 6239) with support for related nematodes:
- B. malayi, C. briggsae, C. brenneri, C. japonica, C. remanei
- P. pacificus, S. ratti, T. muris, O. volvulus

### Database Configuration
- **Production DB**: `intermine_prod_5_287_2` (PostgreSQL)
- **Items DB**: `items-intermine` (build-time temporary database)
- **User Profile DB**: `userprofile_prod` (webapp user data)

### Important File Locations
- Data directory: `/mnt/data/mine_input/datadirWS292` (configurable in project.xml)
- ID resolver cache: `resolver.file.rootpath=/mnt/data2/intermine_dev2/datadir/idresolver`
- Bio-sources: Referenced as `../wormmine-bio-sources/` (external dependency)

## Development Workflow

### Making Data Source Changes
1. Modify source definitions in `project.xml`
2. Update mapping files in `support/properties_xpath/` if needed
3. Run preprocessing: `./support/scripts/deploy/deploy.sh`
4. Rebuild database: `./gradlew clean buildDB`
5. Run post-processing: `./gradlew dbmodel:postprocess`

### Adding New Data Sources
1. Define source in `project.xml` with appropriate type and properties
2. Create mapping file in `support/properties_xpath/`
3. Add preprocessing script in `support/scripts/` if needed
4. Test integration with small dataset first

### Webapp Customization
- Templates: `webapp/src/main/resources/`
- Styling: `webapp/src/main/webapp/themes/wormmine/`
- Configuration: `webapp/src/main/webapp/WEB-INF/`

## Key Technical Details

### InterMine Version Dependencies
- InterMine: 5.0.6
- Bio modules: 5.0.6
- BlueGenes: 1.3.0

### Webapp Configuration
- Context path: `/tools/wormmine`
- Base URL: `http://intermine.wormbase.org`
- Tomcat version: 8.x
- Authentication: Google OAuth2 + local accounts

### Post-Processing Dependencies (Poetry)
```toml
[tool.poetry.dependencies]
sqlalchemy = "^2.0.16"
intermine = "^1.13.0"
psycopg2-binary = "^2.9.6"
```

## Troubleshooting

### Common Issues
- **Build failures**: Check database connectivity in `wormmine.properties`
- **Memory issues**: Increase JVM heap size for large data sources
- **Data conflicts**: Review reject files in data directories
- **Webapp deployment**: Verify Tomcat manager credentials

### Debug Mode
Enable debug mode in `project.xml` source definitions by adding:
```xml
<property name="debug" value="true"/>
```

### Log Files
- Build logs: Check Gradle output
- Webapp logs: Tomcat logs directory
- Data processing: Individual script output