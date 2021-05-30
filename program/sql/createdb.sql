CREATE TABLE orders (
    order_id serial PRIMARY KEY,
    location VARCHAR (255) NOT NULL,
    image_directory VARCHAR (255) UNIQUE,
    created_on timestamptz NOT NULL,
    finished timestamptz,    
    requester_email VARCHAR (255) NOT NULL
);

CREATE TABLE footprints.camera (
    id serial PRIMARY KEY,
    coneid VARCHAR NOT NULL,
    owner VARCHAR (255),
    rotation NUMERIC,
   camid VARCHAR(255) NOT NULL,
    pixelsize DECIMAL,
    imagewidth NUMERIC NOT NULL,
    imageheight NUMERIC NOT NULL,
    focallength DECIMAL
;

INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('501', 'VermessungAVT', 000, 'UC-OpII-1-70918041-f120', 0.0052, 13470, 8670, 82.0000);
INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('502', 'VermessungAVT', 270, 'UC-OpII-1-70918041-f120', 0.0052, 7700, 10300, 123.0000);
INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('503', 'VermessungAVT', 090, 'UC-OpII-1-70918041-f120', 0.0052, 7700, 10300, 123.0000);
INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('504', 'VermessungAVT', 180, 'UC-OpII-1-70918041-f120', 0.0052, 10300, 7700, 123.0000);
INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('505', 'VermessungAVT', 000, 'UC-OpII-1-70918041-f120', 0.0052, 10300, 7700, 123.0000);

INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('82569-50106', 'COWI', 000, 'RCD30_Oblique_Penta_35112', 5.2, 10336, 7788, 53.000);
INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('81559-80195', 'COWI', 000, 'RCD30_Oblique_Penta_35112', 5.2, 10336, 7788, 83.000);
INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('81554-80115', 'COWI', 000, 'RCD30_Oblique_Penta_35112', 5.2, 10336, 7788, 83.000);
INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('81570-80158', 'COWI', 000, 'RCD30_Oblique_Penta_35112', 5.2, 10336, 7788, 83.000);
INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('81572-80117', 'COWI', 000, 'RCD30_Oblique_Penta_35112', 5.2, 10336, 7788, 83.000);

INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('Nadir', 'GeoFly', 270, 'UC-OM3p-423S81560X411059-f120', 5.2, 13470, 8670, 82.0000);
INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('Bwd', 'GeoFly', 270, 'UC-OM3p-423S81560X411059-f120', 5.2, 10300, 7700, 123.0000);
INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('Left', 'GeoFly', 270, 'UC-OM3p-423S81560X411059-f120', 5.2, 7700, 10300, 123.0000);
INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('Fwd', 'GeoFly', 270, 'UC-OM3p-423S81560X411059-f120', 5.2, 10300, 7700, 123.0000);
INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('Right', 'GeoFly', 270, 'UC-OM3p-423S81560X411059-f120', 5.2, 7700, 10300, 123.0000);

INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('501', 'GeoFly', 000, '423S81560X411059-f120', 0.0052, 13470, 8670, 82.0000);
INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('502', 'GeoFly', 270, '423S81560X411059-f120', 0.0052, 7700, 10300, 123.0000);
INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('503', 'GeoFly', 090, '423S81560X411059-f120', 0.0052, 7700, 10300, 123.0000);
INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('504', 'GeoFly', 180, '423S81560X411059-f120', 0.0052, 10300, 7700, 123.0000);
INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('505', 'GeoFly', 000, '423S81560X411059-f120', 0.0052, 10300, 7700, 123.0000);

INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('12339911', 'MGGPAero',000, 'PhaseOne-IXU-RS-1000', 4.6, 11478, 8578, 69.7980);
INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('RS011017', 'MGGPAero',000, 'PhaseOne-IXU-RS-1000', 4.6, 11478, 8578, 108.2837);
INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('RS011009', 'MGGPAero',000, 'PhaseOne-IXU-RS-1000', 4.6, 11478, 8578, 108.2201);
INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('RS011081', 'MGGPAero',000, 'PhaseOne-IXU-RS-1000', 4.6, 11478, 8578, 108.2468);
INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('RS011019', 'MGGPAero',000, 'PhaseOne-IXU-RS-1000', 4.6, 11478, 8578, 108.3599);

INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('C100', 'Terratec',000, 'Osprey-80316002-f120_Rev04.00', 5.2, 13470, 8670, 82.000);
INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('C104', 'Terratec',000, 'Osprey-80316002-f120_Rev04.00', 5.2, 10300, 7700, 122.982);
INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('C105', 'Terratec',000, 'Osprey-80316002-f120_Rev04.00', 5.2, 10300, 7700, 122.980);
INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('C106', 'Terratec',000, 'Osprey-80316002-f120_Rev04.00', 5.2, 10300, 7700, 122.982);
INSERT INTO footprints.camera (coneid, owner, rotation, camid, pixelsize, imagewidth, imageheight, focallength) VALUES ('C107', 'Terratec',000, 'Osprey-80316002-f120_Rev04.00', 5.2, 10300, 7700, 69.7980);
