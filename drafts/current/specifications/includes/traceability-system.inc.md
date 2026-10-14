The BOOST Traceability System implements a comprehensive approach to biomass supply chain tracking that addresses traditional weak points where traceability is lost during material transfers and processing operations.

## Key Implementation Features

### Flexible Identification Framework
TraceableUnit (TRU) entities maintain continuous identification through technology-appropriate methods including trip tickets, RFID tags, QR codes, manual documentation, and emerging biometric signatures. This multi-method approach provides data continuity while accommodating existing industry practices and varying technology readiness levels throughout handling and processing operations.

### Critical Tracking Points
The system establishes standardized measurement and verification infrastructure with flexible configurations. The standard three-point configuration includes:
- **harvest_site** - Initial TRU creation with appropriate identification method and volume measurement
- **consolidation_point** - Transportation consolidation points with reconciliation validation (formerly skid_road/forest_road)
- **mill_entrance** - Processing facility entry points with final verification before transformation

BOOST supports 7 tracking point types total (`harvest_site`, `consolidation_point`, `mill_entrance`, `transfer_station`, `storage_facility`, `quality_control_point`, `mobile_processing_unit`) enabling flexible configurations from 2-point minimum to 5+ point extended setups based on operational complexity.

### Multi-Species Support
Species-specific tracking capabilities enable:
- Individual species identification within mixed material flows
- Species-specific sustainability claim application and inheritance
- Detailed composition tracking with percentage validation
- Regulatory compliance for jurisdiction-specific species requirements

### Complete Processing Chain Documentation
MaterialProcessing entities provide comprehensive audit trails by:
- Linking input TRUs to output TRUs for every transformation
- Tracking plant part changes and transformations during processing
- Validating volume and mass conservation across processing steps
- Supporting split and merge operations with complete lineage tracking

**Lineage.** Lineage is the record of which TraceableUnits an output TraceableUnit was split from or merged from. Each MaterialProcessing record links its input TRUs to its output TRUs, and following those links from a finished unit back to harvest gives its lineage. Lineage is held at the level of units, not of individual kilograms: when units merge, the output's lineage lists every input, and volume and mass conservation checks bound the quantities, but the specification does not attribute each kilogram of the output to a particular input. Claims are allocated across a split by percentage (see ProcessingHistory). Transport does not change lineage: a unit that moves keeps its identifier, and its movements are recorded in LocationHistory.
