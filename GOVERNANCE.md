# Releases and Maintainers

This document sets how BOOST specification releases are versioned and decided, how long a superseded release is supported, and who maintains the specification and its reference software. It operates under the [Charter](BOOST_Charter.org) and the Decision Process defined there; where the two differ, the Charter governs. Tag and build mechanics are in [VERSION.md](VERSION.md).

## Versioning

Releases follow semantic versioning, `MAJOR.MINOR.PATCH`, applied to the specification as a whole: the entity schemas, the JSON-LD context and the specification document.

- **MAJOR**: a change that can make previously valid data invalid, or change its meaning. Removing or renaming an entity, field or enum value; making an optional field required; tightening a pattern, range or format; changing a field's type or semantics.
- **MINOR**: an additive change that leaves all previously valid data valid. New optional fields, new enum values, new entities, new optional relationships.
- **PATCH**: a correction that changes no schema constraint. Descriptions, dictionaries, examples, documentation and fixes to the specification text.

Every release has an entry in [CHANGELOG.md](CHANGELOG.md). A MAJOR release carries migration notes for each breaking change.

## Release decisions

- **MAJOR releases are decided by the group** through the Decision Process: a proposal on the group's list with the changes and migration notes, a discussion period of at least two weeks, then consensus, with the Charter's fallback vote if consensus fails.
- **MINOR and PATCH releases are decided by the Chair** and announced on the group's list with the change log. Any participant may ask, within seven days of the announcement, that a MINOR release go to the group instead; it then follows the MAJOR route.

A Chair decision on a release that touches the Chair's own funded work is disclosed in the announcement.

## Support for the prior version

When a MAJOR release ships, the previous MAJOR version is supported for twelve months: corrections are issued as PATCH releases of that version where an implementer needs them, and its published schemas stay at their stable addresses. After the support window, the schemas remain published and unchanged; no further releases are made.

## Maintainers

The specification and its reference software have two named maintainers, so that neither depends on one person:

- Peter Tittmann (Arbos)
- Dan Sanchez (University of California, Berkeley)

Maintainers merge changes the group has accepted, cut and tag releases decided under this document, and keep the published schemas and documentation at stable addresses. Either maintainer can cut a release. Maintainers are named, replaced or added by the group through the Decision Process.

## Changing this document

This document is changed through the Decision Process.
