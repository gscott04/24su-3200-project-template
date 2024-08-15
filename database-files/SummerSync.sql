DROP DATABASE IF EXISTS summersync;
CREATE DATABASE IF NOT EXISTS summersync;
USE summersync;

DROP TABLE IF EXISTS Guardian;
CREATE TABLE IF NOT EXISTS Guardian (
    guardianID int PRIMARY KEY,
    firstName varchar(25) NOT NULL,
    lastName varchar(25) NOT NULL,
    email varchar(30) NOT NULL,
    phone varchar(20) NOT NULL,
    paid boolean DEFAULT 0
);

DROP TABLE IF EXISTS Admin;
CREATE TABLE IF NOT EXISTS Admin (
    adminID int PRIMARY KEY,
    firstName varchar(25) NOT NULL,
    lastName varchar(25) NOT NULL,
    email varchar(30) NOT NULL,
    phone varchar(20) NOT NULL
);

DROP TABLE IF EXISTS Location;
CREATE TABLE IF NOT EXISTS Location (
    locationID int PRIMARY KEY,
    region varchar(50) NOT NULL,
    territory varchar(50) NOT NULL,
    adminID int NOT NULL,

    CONSTRAINT fk_Location_adminID FOREIGN KEY (adminID)
        REFERENCES Admin (adminID)
        ON UPDATE cascade ON DELETE restrict
);

DROP TABLE IF EXISTS Camp;
CREATE TABLE IF NOT EXISTS Camp (
    campID int PRIMARY KEY,
    campName varchar(70) NOT NULL,
    capacity int NOT NULL,
    campDirectorID int NOT NULL,
    active boolean DEFAULT 0 NOT NULL,
    description text,
    phone varchar(20) NOT NULL,
    email varchar(30) NOT NULL
);

DROP TABLE IF EXISTS CampSession;
CREATE TABLE IF NOT EXISTS CampSession (
    sessionID int NOT NULL,
    campID int NOT NULL,
    startDate date NOT NULL,
    endDate date NOT NULL,
    sessionType boolean DEFAULT 0,

    PRIMARY KEY (sessionID, campID),
    CONSTRAINT fk_CampSession_campID FOREIGN KEY (campID)
        REFERENCES Camp (campID)
        ON UPDATE restrict ON DELETE restrict
);

DROP TABLE IF EXISTS Staff;
CREATE TABLE IF NOT EXISTS Staff (
    staffID int PRIMARY KEY,
    firstName varchar(25) NOT NULL,
    lastName varchar(25) NOT NULL,
    role varchar(40) NOT NULL,
    phoneNumber varchar(20) NOT NULL,
    email varchar(30) NOT NULL,
    sessionID int NOT NULL,
    campID int NOT NULL,

    CONSTRAINT fk_Staff_sessionID_campID FOREIGN KEY (sessionID, campID)
        REFERENCES CampSession (sessionID, campID)
        ON UPDATE cascade ON DELETE restrict
);

DROP TABLE IF EXISTS Cabin;
CREATE TABLE IF NOT EXISTS Cabin (
    cabinID int PRIMARY KEY,
    cabinName varchar(50),
    staffID int NOT NULL UNIQUE,
    capacity int NOT NULL,

    CONSTRAINT fk_Cabin_staffID FOREIGN KEY (staffID)
        REFERENCES Staff (staffID)
        ON UPDATE cascade ON DELETE restrict
);

DROP TABLE IF EXISTS Bed;
CREATE TABLE IF NOT EXISTS Bed (
    bedID int NOT NULL,
    cabinID int NOT NULL,

    PRIMARY KEY (bedID, cabinID),
    CONSTRAINT fk_Bed_cabinID FOREIGN KEY (cabinID)
        REFERENCES Cabin (cabinID)
        ON UPDATE cascade ON DELETE restrict
);

DROP TABLE IF EXISTS MedicalInfo;
CREATE TABlE IF NOT EXISTS MedicalInfo (
    medID int PRIMARY KEY,
    type varchar(30) NOT NULL
);

DROP TABLE IF EXISTS Camper;
CREATE TABLE IF NOT EXISTS Camper (
    camperID int PRIMARY KEY,
    firstName varchar(25) NOT NULL,
    lastName varchar(25) NOT NULL,
    campID int NOT NULL,
    DOB date NOT NULL,
    guardianID int NOT NULL,
    bedID int NOT NULL,
    cabinID int NOT NULL,
    staffID int NOT NULL,

    CONSTRAINT fk_Camper_campID FOREIGN KEY (campID)
        REFERENCES Camp (campID)
        ON UPDATE cascade ON DELETE restrict,
    CONSTRAINT fk_Camper_guardianID FOREIGN KEY (guardianID)
        REFERENCES Guardian (guardianID)
        ON UPDATE cascade ON DELETE restrict,
    CONSTRAINT fk_Camper_bedID_cabinID FOREIGN KEY (bedID, cabinID)
        REFERENCES Bed (bedID, cabinID)
        ON UPDATE cascade ON DELETE restrict,
    CONSTRAINT fk_Camper_staffID FOREIGN KEY (staffID)
        REFERENCES Cabin (staffID)
        ON UPDATE cascade ON DELETE restrict
);

DROP TABLE IF EXISTS DailySchedule;
CREATE TABLE IF NOT EXISTS DailySchedule (
    scheduleID int PRIMARY KEY,
    date DATE NOT NULL,
    time TIME NOT NULL,
    campID int NOT NULL,
    sessionID int NOT NULL,

    CONSTRAINT fk_DailySchedule_campID FOREIGN KEY (sessionID, campID)
        REFERENCES CampSession (sessionID, campID)
        ON UPDATE cascade ON DELETE restrict
);

DROP TABLE IF EXISTS Activity;
CREATE TABLE IF NOT EXISTS Activity (
    activityID int PRIMARY KEY,
    name varchar(30) NOT NULL,
    description TEXT NOT NULL
);

DROP TABLE IF EXISTS MedNeeds;
CREATE TABLE IF NOT EXISTS MedNeeds (
    medID int NOT NULL,
    camperID int NOT NULL,

    PRIMARY KEY (medID, camperID),
    CONSTRAINT fk_MedNeeds_medID FOREIGN KEY (medID)
        REFERENCES MedicalInfo (medID)
        ON UPDATE cascade ON DELETE restrict,
    CONSTRAINT fk_MedNeeds_camperID FOREIGN KEY (camperID)
        REFERENCES Camper (camperID)
        ON UPDATE cascade ON DELETE restrict
);

DROP TABLE IF EXISTS CampLoc;
CREATE TABLE IF NOT EXISTS CampLoc (
    campID int NOT NULL,
    locationID int NOT NULL,

    PRIMARY KEY (campID, locationID),
    CONSTRAINT fk_CampLoc_campID FOREIGN KEY (campID)
        REFERENCES Camp (campID)
        ON UPDATE cascade ON DELETE restrict,
    CONSTRAINT fk_CampLoc_locationID FOREIGN KEY (locationID)
        REFERENCES Location (locationID)
        ON UPDATE cascade ON DELETE restrict
);

DROP TABLE IF EXISTS ScheduleActivity;
CREATE TABLE IF NOT EXISTS ScheduleActivity (
    activityID int NOT NULL,
    scheduleID int NOT NULL,

    PRIMARY KEY (activityID, scheduleID),
    CONSTRAINT fk_ScheduleActivity_activityID FOREIGN KEY (activityID)
        REFERENCES Activity (activityID)
        ON UPDATE cascade ON DELETE restrict,
    CONSTRAINT fk_ScheduleActivity_scheduleID FOREIGN KEY (scheduleID)
        REFERENCES DailySchedule (scheduleID)
        ON UPDATE cascade ON DELETE restrict
);

DROP TABLE IF EXISTS RequiredItems;
CREATE TABLE IF NOT EXISTS RequiredItems (
    requiredItems varchar(30),
    activityID int,

    PRIMARY KEY (requiredItems, activityID),
    CONSTRAINT fk_RequiredItems_activityID FOREIGN KEY (activityID)
        REFERENCES Activity (activityID)
        ON UPDATE cascade ON DELETE restrict
);

INSERT INTO Guardian (guardianID, firstName, lastName, email, phone, paid) VALUES
(1, 'Katy', 'Ito', 'katyito@example.com', '154-669-8535', false),
(2, 'Cello', 'Matijevic', 'cmatijevic1@example.com', '175-692-0136', false),
(3, 'Tabbie', 'Bestman', 'tbestman2@example.com', '767-650-3379', false),
(4, 'Alfons', 'Symmons', 'asymmons3@example.com', '363-623-9076', false),
(5, 'Anastasie', 'Bunn', 'abunn4@example.com', '359-824-1239', true),
(6, 'Maxie', 'Hartland', 'mhartland5@example.com', '305-867-1169', false),
(7, 'Dinnie', 'Tayt', 'dtayt6@example.com', '249-271-7971', false),
(8, 'Rhetta', 'Gounet', 'rgounet7@example.com', '835-593-8796', true),
(9, 'Rollin', 'Unworth', 'runworth8@example.com', '979-473-6990', false),
(10, 'Tiff', 'Hyndman', 'thyndman9@example.com', '330-392-8711', true),
(11, 'Flori', 'Burl', 'fburla@example.com', '748-186-1654', true),
(12, 'Meredithe', 'Sooper', 'msooperb@example.com', '183-319-0427', true),
(13, 'Thea', 'Carlo', 'tcarloc@example.com', '607-590-3125', true),
(14, 'Karissa', 'Clemas', 'kclemasd@example.com', '973-605-3073', true),
(15, 'Thor', 'Cristofvao', 'tcristofvaoe@example.com', '886-148-6953', true),
(16, 'Pearline', 'MacCurlye', 'pmaccurlyef@example.com', '777-493-3832', false),
(17, 'Minne', 'Vokes', 'mvokesg@example.com', '649-721-9403', false),
(18, 'Yard', 'Firmin', 'yfirminh@example.com', '268-350-4284', true),
(19, 'Tonnie', 'Basill', 'tbasilli@example.com', '138-463-9286', true),
(20, 'Tyler', 'Keirl', 'tkeirlj@example.com', '737-232-5249', false),
(21, 'Antonietta', 'Sommerly', 'asommerlyk@example.com', '179-893-3121', true),
(22, 'Bobbette', 'Mulcock', 'bmulcockl@example.com', '921-452-0516', false),
(23, 'Nessy', 'Dearlove', 'ndearlovem@example.com', '651-737-9240', true),
(24, 'Burton', 'Waterstone', 'bwaterstonen@example.com', '312-247-3200', true),
(25, 'Noemi', 'Gummery', 'ngummeryo@example.com', '823-881-9429', false),
(26, 'Janean', 'Mattiussi', 'jmattiussip@example.com', '422-822-6709', false),
(27, 'Marika', 'Cliffe', 'mcliffeq@example.com', '782-106-3468', true),
(28, 'Bartel', 'Seers', 'bseersr@example.com', '585-560-0841', false),
(29, 'Shelli', 'Regi', 'sregis@example.com', '294-954-6975', false),
(30, 'Afton', 'MacDonell', 'amacdonellt@example.com', '347-320-3441', true),
(31, 'Rosalinda', 'Woodison', 'rwoodisonu@example.com', '572-973-2582', true),
(32, 'Finlay', 'Boater', 'fboaterv@example.com', '730-653-2163', false),
(33, 'Eirena', 'Greg', 'egregw@example.com', '254-833-9736', true),
(34, 'Honey', 'O''Devey', 'hodeveyx@example.com', '463-917-1637', false),
(35, 'Alexandro', 'Dencs', 'adencsy@example.com', '638-344-9078', true),
(36, 'Helen-elizabeth', 'Tiptaft', 'htiptaftz@example.com', '396-218-8059', true),
(37, 'Brandy', 'Bindon', 'bbindon10@example.com', '463-193-6261', true),
(38, 'Dedie', 'Dutt', 'ddutt11@example.com', '390-423-4728', true),
(39, 'Carroll', 'Mc Andrew', 'cmcandrew12@example.com', '601-423-0274', false),
(40, 'Shel', 'Olenchikov', 'solenchikov13@example.com', '958-489-3916', false);

INSERT INTO Camp (active, campID, campName, capacity, campDirectorID, phone, email)
VALUES (1, 34098, 'PrimeTime', 900, 87620, '908-320-6572', 'primeT@email.com'),
       (0, 56041, 'LagoonLife', 150,  09382, '981-342-8701', 'L.Lagoon@email.com');

INSERT INTO CampSession (sessionID, campID, startDate, endDate, sessionType)
VALUES (1, 34098, '2024-07-31', '2024-08-14', 1),
       (2, 56041, '2024-07-15', '2024-07-15', 1);

INSERT INTO Staff (staffID, firstName, lastName, role, phoneNumber, email, sessionID, campID)
VALUES (1, 'Jackie', 'Jones', 'counselor', '508-111-2344', 'jjones@gmail.com', 1, 34098),
       (2, 'Hailey', 'Potts', 'cook', '453-545-2734', 'hpotts@gmail.com', 2, 56041);

INSERT INTO Admin
VALUES (2390, 'Steve', 'Smith', 'ssmith@email.com', '756-322-6456'),
       (8673509, 'Sashana', 'Bean', 'sbean@email.com', '345-624-1987');

INSERT INTO Location (region, territory, locationID, adminID)
VALUES ('Southwest', 'Texas', 2890, 02390),
       ('Northwest', 'Washington', 4936, 8673509);

INSERT INTO CampLoc (campID, locationID)
VALUES (56041, 4936),
       (34098, 2890);

INSERT INTO MedicalInfo (medID, type)
VALUES (1, 'Allergy'),
       (2, 'Asthma');

INSERT INTO Cabin (cabinID, cabinName, staffID, capacity)
VALUES (501, 'Cabin 1', 1, 10),
       (502, 'Cabin 2', 2, 15);

INSERT INTO Bed (bedID, cabinID)
VALUES (401, 501),
       (402, 502);

INSERT INTO Camper (camperID, firstName, lastName, campID, DOB, guardianID, bedID, cabinID, staffID)
VALUES (1, 'John', 'Doe',34098 , '2010-06-15', 1, 401, 501, 1),
       (2, 'Jane', 'Smith', 34098, '2011-04-20', 2, 402, 502, 1);

INSERT INTO MedNeeds(medID, camperID)
VALUES (1, 1),
       (2, 2);

INSERT INTO DailySchedule (scheduleID, sessionID, campID, date, time)
VALUES (03, 1, 34098, '2015-08-08', '11:05:00'),
       (05, 2, 56041, '2016-07-29', '12:35:00');

INSERT INTO Activity (activityID, name, description)
VALUES (1, 'Swimming', 'Pool 3'),
       (2, 'Biking', 'At the Park');

INSERT INTO RequiredItems(requiredItems, activityID)
VALUES ('pool noodle', 1),
       ('bike', 2);

INSERT INTO ScheduleActivity(activityID, scheduleID)
VALUES (1, 03),
      (2, 05);


