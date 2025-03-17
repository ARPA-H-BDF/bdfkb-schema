-- # Class: "NamedThing" Description: "A generic grouping for any identifiable entity"
--     * Slot: id Description: A unique identifier for a thing.
--     * Slot: name Description: A human-readable name for a thing.
--     * Slot: description Description: A human-readable description for a thing.
-- # Class: "Tool" Description: ""
--     * Slot: id Description: A unique identifier for a thing.
--     * Slot: name Description: A human-readable name for a thing.
--     * Slot: description Description: A human-readable description for a thing.

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Tool" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);