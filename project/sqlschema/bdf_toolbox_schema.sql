-- # Class: "NamedThing" Description: "A generic grouping for any identifiable entity"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "Tool" Description: "Represents a Tool"
--     * Slot: developer_team Description: BDF performer team
--     * Slot: technical_area Description: BDF Technical Area
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: ToolCollection_id Description: Autocreated FK slot
-- # Class: "ToolCollection" Description: "A holder for Tool objects"
--     * Slot: id Description: 

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ToolCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Tool" (
	developer_team VARCHAR(14), 
	technical_area VARCHAR(3), 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"ToolCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("ToolCollection_id") REFERENCES "ToolCollection" (id)
);