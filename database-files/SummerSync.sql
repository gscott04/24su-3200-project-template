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

INSERT INTO Camp (campID, campName, capacity, campDirectorID, active, description, phone, email) VALUES 
(1, 'Tropical Ladies''-tresses', 990, 1, true, 'In hac habitasse platea dictumst. Maecenas ut massa quis augue luctus tincidunt. Nulla mollis molestie lorem.', '892-747-4424', 'timesson0@camp.org'),
(2, 'Dense Logwood', 581, 2, true, 'Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis. Fusce posuere felis sed lacus.', '420-208-7314', 'mchurchill1@camp.org'),
(3, 'Palmer''s Groundcherry', 514, 3, false, 'Duis consequat dui nec nisi volutpat eleifend.', '858-494-7631', 'cdomnick2@camp.org'),
(4, 'Hairy Clematis', 335, 4, false, 'Mauris sit amet eros.', '418-302-0640', 'gpentony3@camp.org'),
(5, 'Coastal Bluff Bentgrass', 866, 5, true, 'Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci.', '827-460-6546', 'pkimbury4@camp.org'),
(6, 'Broadleaf Ironweed', 54, 6, false, 'Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.', '764-510-2043', 'gpengilly5@camp.org'),
(7, 'Woodland Sage', 813, 7, true, 'Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem. Integer tincidunt ante vel ipsum.', '483-484-4127', 'ssprowles6@camp.org'),
(8, 'Arkansas Bedstraw', 548, 8, true, 'Morbi ut odio. Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo.', '973-322-0587', 'dsehorsch7@camp.org'),
(9, 'Java Plum', 333, 9, false, 'Sed sagittis.', '445-414-7272', 'sbaselli8@camp.org'),
(10, 'Rhodobryum Moss', 989, 10, true, 'In est risus, auctor sed, tristique in, tempus sit amet, sem.', '908-393-2384', 'msamper9@camp.org'),
(11, 'Platycodon', 248, 11, false, 'Nulla tellus.', '234-331-6055', 'rimlawa@camp.org'),
(12, 'Harper''s Dodder', 525, 12, false, 'Donec semper sapien a libero.', '832-235-2288', 'jdoerlingb@camp.org'),
(13, 'Yellowwood', 696, 13, true, 'Etiam justo.', '440-621-0208', 'kgillonc@camp.org'),
(14, 'Mt. Lassen Fleabane', 231, 14, false, 'Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum. Curabitur in libero ut massa volutpat convallis.', '510-464-8832', 'aabrahmd@camp.org'),
(15, 'Stemmy Four-nerve Daisy', 352, 15, false, 'Quisque porta volutpat erat.', '162-143-9293', 'blukasene@camp.org'),
(16, 'Henssen''s Map Lichen', 229, 16, true, 'Curabitur convallis. Duis consequat dui nec nisi volutpat eleifend.', '777-194-2647', 'lchapelhowf@camp.org'),
(17, 'Sandberg Bluegrass', 443, 17, true, 'Proin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem.', '555-442-3135', 'btheyerg@camp.org'),
(18, 'Yellow Bur Pincushionplant', 955, 18, false, 'In hac habitasse platea dictumst.', '911-542-3671', 'limlackeh@camp.org'),
(19, 'Bolander''s Silene', 95, 19, false, 'Suspendisse potenti. Nullam porttitor lacus at turpis.', '626-481-9619', 'tmockfordi@camp.org'),
(20, 'Orange Agoseris', 77, 20, false, 'Nunc nisl.', '350-940-3914', 'bwollacottj@camp.org'),
(21, 'Tufted Bulrush', 463, 21, false, 'Nunc nisl. Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. Donec dapibus.', '244-628-3598', 'dgilderk@camp.org'),
(22, 'Tampa Mock Vervain', 930, 22, true, 'Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.', '459-704-2798', 'msollowayel@camp.org'),
(23, 'Cupgrass', 266, 23, false, 'Nulla nisl. Nunc nisl. Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa.', '933-936-9079', 'fstrobanm@camp.org'),
(24, 'Manyray Aster', 434, 24, false, 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Proin risus.', '759-117-6873', 'bpetracchin@camp.org'),
(25, 'Diffuse Knapweed', 354, 25, false, 'Quisque erat eros, viverra eget, congue eget, semper rutrum, nulla. Nunc purus. Phasellus in felis.', '420-556-8409', 'adamiralo@camp.org'),
(26, 'Tall Bluebells', 572, 26, true, 'Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.', '802-482-7289', 'dgilbankp@camp.org'),
(27, 'San Clemente Island Triteleia', 955, 27, false, 'In congue. Etiam justo.', '405-358-0915', 'showlesq@camp.org'),
(28, 'Rattlebox', 303, 28, true, 'Nunc rhoncus dui vel sem. Sed sagittis.', '202-292-4467', 'ctreverr@camp.org'),
(29, 'Leechbush', 838, 29, false, 'Etiam vel augue.', '207-415-9874', 'bbauldreys@camp.org'),
(30, 'Farewell To Spring', 662, 30, false, 'Integer ac leo.', '684-119-0175', 'nmackettt@camp.org'),
(31, 'Rayless Arnica', 350, 31, true, 'Aenean auctor gravida sem. Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo.', '499-561-3348', 'wtoppu@camp.org'),
(32, 'Loving Sedge', 746, 32, false, 'Donec semper sapien a libero. Nam dui.', '748-450-8815', 'stabourelv@camp.org'),
(33, 'Leonard''s Skullcap', 184, 33, true, 'Etiam faucibus cursus urna. Ut tellus. Nulla ut erat id mauris vulputate elementum.', '807-788-6435', 'craynesw@camp.org'),
(34, 'Clustered Frostweed', 339, 34, false, 'Phasellus sit amet erat.', '627-217-3400', 'ddevilx@camp.org'),
(35, 'Eastern Purple Bladderwort', 390, 35, true, 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit.', '428-271-8081', 'fbiddulphy@camp.org'),
(36, 'Great Basin Brome', 118, 36, true, 'In hac habitasse platea dictumst. Morbi vestibulum, velit id pretium iaculis, diam erat fermentum justo, nec condimentum neque sapien placerat ante.', '615-311-5372', 'jmccowanz@camp.org'),
(37, 'Trichothelium Lichen', 941, 37, true, 'Suspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst.', '517-346-6693', 'spencot10@camp.org'),
(38, 'Ornduff''s Goldfields', 76, 38, false, 'Aliquam quis turpis eget elit sodales scelerisque. Mauris sit amet eros.', '598-531-0298', 'vcurtoys11@camp.org'),
(39, 'Red Star Apple', 219, 39, false, 'Duis at velit eu est congue elementum. In hac habitasse platea dictumst.', '371-191-7413', 'hgamet12@camp.org'),
(40, 'Eyed Gilia', 643, 40, true, 'Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus.', '313-749-4830', 'bgatfield13@camp.org');
;

INSERT INTO CampSession (sessionID, campID, startDate, endDate, sessionType) VALUES
(1, '1', '2024-07-22', '2024-08-25', false),
(2, '2', '2024-07-22', '2024-08-05', true),
(3, '3', '2024-07-22', '2024-08-24', false),
(4, '4', '2024-07-22', '2024-08-21', true),
(5, '5', '2024-07-26', '2024-08-18', true),
(6, '6', '2024-07-22', '2024-08-01', false),
(7, '7', '2024-07-22', '2024-08-27', true),
(8, '8', '2024-07-22', '2024-08-04', true),
(9, '9', '2024-07-22', '2024-08-26', false),
(10, '10', '2024-07-22', '2024-08-20', true),
(11, '11', '2024-07-22', '2024-08-12', false),
(12, '12', '2024-07-22', '2024-08-27', true),
(13, '13', '2024-07-22', '2024-08-14', false),
(14, '14', '2024-07-22', '2024-08-13', false),
(15, '15', '2024-07-22', '2024-08-17', true),
(16, '16', '2024-07-26', '2024-08-12', false),
(17, '17', '2024-07-22', '2024-08-04', true),
(18, '18', '2024-07-22', '2024-08-26', false),
(19, '19', '2024-07-22', '2024-08-01', true),
(20, '20', '2024-07-22', '2024-08-06', false),
(21, '21', '2024-07-22', '2024-08-08', false),
(22, '22', '2024-07-22', '2024-08-18', true),
(23, '23', '2024-07-22', '2024-08-31', true),
(24, '24', '2024-07-22', '2024-08-30', true),
(25, '25', '2024-07-22', '2024-08-10', false),
(26, '26', '2024-07-26', '2024-08-20', true),
(27, '27', '2024-07-22', '2024-08-21', true),
(28, '28', '2024-07-22', '2024-08-14', false),
(29, '29', '2024-07-22', '2024-08-26', true),
(30, '30', '2024-07-22', '2024-08-12', true),
(31, '31', '2024-07-27', '2024-08-19', false),
(32, '32', '2024-07-22', '2024-08-12', true),
(33, '33', '2024-07-22', '2024-08-14', false),
(34, '34', '2024-07-22', '2024-08-11', true),
(35, '35', '2024-07-22', '2024-08-06', false),
(36, '36', '2024-07-22', '2024-08-25', true),
(37, '37', '2024-07-22', '2024-08-13', true),
(38, '38', '2024-07-22', '2024-08-11', true),
(39, '39', '2024-07-25', '2024-08-24', false),
(40, '40', '2024-07-22', '2024-08-17', false),
(41, '1', '2024-07-22', '2024-08-08', true),
(42, '2', '2024-07-26', '2024-08-02', false),
(43, '3', '2024-07-29', '2024-08-03', true),
(44, '4', '2024-07-22', '2024-08-22', true),
(45, '5', '2024-07-22', '2024-08-27', false),
(46, '6', '2024-07-29', '2024-08-31', false),
(47, '7', '2024-07-22', '2024-08-02', true),
(48, '8', '2024-07-22', '2024-08-16', false),
(49, '9', '2024-07-22', '2024-08-14', false),
(50, '10', '2024-07-24', '2024-08-13', false);

INSERT INTO Staff (staffID, firstName, lastName, role, phoneNumber, email, sessionID, campID) VALUES
(1, 'Jackie', 'Jones', 'Camp Director', '879-805-9007', 'jjones@camp.com', '1', '1'),
(2, 'Jacenta', 'Ruddock', 'Nature Guide', '212-146-8254', 'jruddock1@camp.com', '2', '2'),
(3, 'Kevina', 'McKeefry', 'Activity Leader', '709-152-1460', 'kmckeefry2@camp.com', '3', '3'),
(4, 'Arlyn', 'Ratnage', 'Camp Photographer', '200-100-6064', 'aratnage3@camp.com', '4', '4'),
(5, 'Temple', 'Carrol', 'Camp Counselor', '164-641-1693', 'tcarrol4@camp.com', '5', '5'),
(6, 'Rica', 'Polendine', 'Camp Counselor', '547-705-2752', 'rpolendine5@camp.com', '6', '6'),
(7, 'Clarissa', 'Farey', 'Arts and Crafts Instructor', '587-287-3643', 'cfarey6@camp.com', '7', '7'),
(8, 'Kort', 'Fallanche', 'Camp Photographer', '174-851-1813', 'kfallanche7@camp.com', '8', '8'),
(9, 'Mill', 'Osgood', 'Camp Photographer', '761-328-9790', 'mosgood8@camp.com', '9', '9'),
(10, 'Joice', 'Aberchirder', 'Activity Leader', '949-556-6785', 'jaberchirder9@camp.com', '10', '10'),
(11, 'Ethyl', 'Allflatt', 'Camp Photographer', '875-849-8349', 'eallflatta@camp.com', '11', '11'),
(12, 'Angelia', 'Dilawey', 'Camp Director', '935-197-5146', 'adilaweyb@camp.com', '12', '12'),
(13, 'Nicol', 'Abrahamsohn', 'Camp Nurse', '926-876-5290', 'nabrahamsohnc@camp.com', '13', '13'),
(14, 'Ron', 'Spering', 'Camp Photographer', '516-760-8824', 'rsperingd@camp.com', '14', '14'),
(15, 'Towney', 'Hobgen', 'Nature Guide', '192-451-5706', 'thobgene@camp.com', '15', '15'),
(16, 'Clarey', 'Wildt', 'Camp Counselor', '530-540-9430', 'cwildtf@camp.com', '16', '16'),
(17, 'Marrilee', 'Sleith', 'Outdoor Adventure Specialist', '699-873-8090', 'msleithg@camp.com', '17', '17'),
(18, 'Jerrilyn', 'Mosey', 'Outdoor Adventure Specialist', '517-841-7392', 'jmoseyh@camp.com', '18', '18'),
(19, 'Jordan', 'Chilvers', 'Lifeguard', '603-961-9363', 'jchilversi@camp.com', '19', '19'),
(20, 'Mahalia', 'Clashe', 'Nature Guide', '521-411-5293', 'mclashej@camp.com', '20', '20'),
(21, 'Tessie', 'Brobak', 'Lifeguard', '141-167-9382', 'tbrobakk@camp.com', '21', '21'),
(22, 'Dur', 'Maidens', 'Arts and Crafts Instructor', '377-311-1247', 'dmaidensl@camp.com', '22', '22'),
(23, 'Claiborn', 'Danbi', 'Camp Nurse', '362-636-4434', 'cdanbim@camp.com', '23', '23'),
(24, 'Lem', 'Busswell', 'Camp Counselor', '451-318-2342', 'lbusswelln@camp.com', '24', '24'),
(25, 'Norean', 'Dugald', 'Camp Counselor', '837-541-6631', 'ndugaldo@camp.com', '25', '25'),
(26, 'Silvester', 'Licas', 'Activity Leader', '717-364-0013', 'slicasp@camp.com', '26', '26'),
(27, 'Finn', 'Bru', 'Outdoor Adventure Specialist', '186-983-7074', 'fbruq@camp.com', '27', '27'),
(28, 'Son', 'Speller', 'Outdoor Adventure Specialist', '414-996-4521', 'sspellerr@camp.com', '28', '28'),
(29, 'Wiatt', 'Eltringham', 'Lifeguard', '612-930-1104', 'weltringhams@camp.com', '29', '29'),
(30, 'Juliann', 'McGrirl', 'Activity Leader', '599-473-1702', 'jmcgrirlt@camp.com', '30', '30'),
(31, 'Klara', 'D''eath', 'Nature Guide', '304-722-6522', 'kdeathu@camp.com', '31', '31'),
(32, 'Rube', 'Snodin', 'Camp Counselor', '440-239-4134', 'rsnodinv@camp.com', '32', '32'),
(33, 'Letizia', 'Chown', 'Lifeguard', '630-158-0457', 'lchownw@camp.com', '33', '33'),
(34, 'Gerick', 'Ginni', 'Camp Counselor', '838-459-2684', 'gginnix@camp.com', '34', '34'),
(35, 'Dody', 'Matkovic', 'Camp Counselor', '872-323-9719', 'dmatkovicy@camp.com', '35', '35'),
(36, 'Shaina', 'O''Farrell', 'Outdoor Adventure Specialist', '593-866-5266', 'sofarrellz@camp.com', '36', '36'),
(37, 'Lyndsey', 'Wiskar', 'Nature Guide', '285-390-5017', 'lwiskar10@camp.com', '37', '37'),
(38, 'Walden', 'Brundell', 'Lifeguard', '415-341-3264', 'wbrundell11@camp.com', '38', '38'),
(39, 'Emmit', 'Fellgatt', 'Activity Leader', '858-777-4197', 'efellgatt12@camp.com', '39', '39'),
(40, 'Opaline', 'Cessford', 'Camp Photographer', '503-503-2641', 'ocessford13@camp.com', '40', '40'),
(41, 'Corny', 'Houliston', 'Camp Director', '762-384-1925', 'chouliston14@camp.com', '41', '1'),
(42, 'Arlene', 'Brimblecombe', 'Nature Guide', '935-762-8431', 'abrimblecombe15@camp.com', '42', '2'),
(43, 'Jeanine', 'Dufaur', 'Camp Counselor', '541-909-3622', 'jdufaur16@camp.com', '43', '3'),
(44, 'Merill', 'Kynvin', 'Activity Leader', '308-293-7484', 'mkynvin17@camp.com', '44', '4'),
(45, 'Kip', 'Holtaway', 'Lifeguard', '469-718-5531', 'kholtaway18@camp.com', '45', '5'),
(46, 'Arlina', 'Fawdry', 'Arts and Crafts Instructor', '792-584-6106', 'afawdry19@camp.com', '46', '6'),
(47, 'Midge', 'Swinyard', 'Camp Nurse', '615-347-9270', 'mswinyard1a@camp.com', '47', '7'),
(48, 'Arlette', 'Brimner', 'Camp Photographer', '408-663-5339', 'abrimner1b@camp.com', '48', '8'),
(49, 'Marysa', 'Ghelerdini', 'Outdoor Adventure Specialist', '282-315-7334', 'mghelerdini1c@camp.com', '49', '9'),
(50, 'Arlene', 'Prendeville', 'Camp Counselor', '719-584-2974', 'aprendeville1d@camp.com', '50', '10'),
(51, 'Kirstyn', 'Goulbourn', 'Camp Director', '305-768-1429', 'kgoulbourn1e@camp.com', '1', '1'),
(52, 'Corny', 'Brimacombe', 'Nature Guide', '937-453-8730', 'cbrimacombe1f@camp.com', '2', '2'),
(53, 'Arlene', 'Goulding', 'Camp Counselor', '618-334-5279', 'agoulding1g@camp.com', '3', '3'),
(54, 'Merill', 'Kynston', 'Activity Leader', '409-885-7123', 'mkynston1h@camp.com', '4', '4'),
(55, 'Kip', 'Holton', 'Lifeguard', '570-229-8173', 'kholton1i@camp.com', '5', '5'),
(56, 'Arlina', 'Fawcett', 'Arts and Crafts Instructor', '793-695-7217', 'afawcett1j@camp.com', '6', '6'),
(57, 'Midge', 'Swinhoe', 'Camp Nurse', '716-458-0381', 'mswinhoe1k@camp.com', '7', '7'),
(58, 'Arlette', 'Brimstin', 'Camp Photographer', '509-774-6450', 'abrimstin1l@camp.com', '8', '8'),
(59, 'Marysa', 'Gheerhaert', 'Outdoor Adventure Specialist', '383-426-8445', 'mgheerhaert1m@camp.com', '9', '9'),
(60, 'Arlene', 'Prentice', 'Camp Counselor', '820-695-3085', 'aprentice1n@camp.com', '10', '10'),
(61, 'Kirstyn', 'Gouldsmith', 'Camp Director', '406-879-2540', 'kgouldsmith1o@camp.com', '11', '11'),
(62, 'Corny', 'Brimacomber', 'Nature Guide', '938-564-9841', 'cbrimacomber1p@camp.com', '12', '12'),
(63, 'Arlene', 'Gouldstraw', 'Camp Counselor', '719-445-6390', 'agouldstraw1q@camp.com', '13', '13'),
(64, 'Merill', 'Kynaston', 'Activity Leader', '510-996-8234', 'mkynaston1r@camp.com', '14', '14'),
(65, 'Kip', 'Holtom', 'Lifeguard', '671-330-9285', 'kholtom1s@camp.com', '15', '15'),
(66, 'Arlina', 'Fawkes', 'Arts and Crafts Instructor', '894-706-8328', 'afawkes1t@camp.com', '16', '16'),
(67, 'Midge', 'Swinley', 'Camp Nurse', '817-569-1492', 'mswinley1u@camp.com', '17', '17'),
(68, 'Arlette', 'Brimson', 'Camp Photographer', '610-885-7561', 'abrimson1v@camp.com', '18', '18'),
(69, 'Marysa', 'Ghiotto', 'Outdoor Adventure Specialist', '484-537-9556', 'mghiotto1w@camp.com', '19', '19'),
(70, 'Arlene', 'Prentout', 'Camp Counselor', '921-706-4196', 'aprentout1x@camp.com', '20', '20'),
(71, 'Kirstyn', 'Goulter', 'Camp Director', '507-980-3651', 'kgoulter1y@camp.com', '21', '21'),
(72, 'Corny', 'Brimat', 'Nature Guide', '939-675-0952', 'cbrimat1z@camp.com', '22', '22'),
(73, 'Arlene', 'Goulthorp', 'Camp Counselor', '820-556-7401', 'agoulthorp20@camp.com', '23', '23'),
(74, 'Merill', 'Kynoch', 'Activity Leader', '611-107-9345', 'mkynoch21@camp.com', '24', '24'),
(75, 'Kip', 'Holttom', 'Lifeguard', '772-441-0396', 'kholttom22@camp.com', '25', '25'),
(76, 'Arlina', 'Fawkner', 'Arts and Crafts Instructor', '995-817-9439', 'afawkner23@camp.com', '26', '26'),
(77, 'Midge', 'Swinney', 'Camp Nurse', '918-670-2503', 'mswinney24@camp.com', '27', '27'),
(78, 'Arlette', 'Brimble', 'Camp Photographer', '711-996-8672', 'abrimble25@camp.com', '28', '28'),
(79, 'Marysa', 'Ghioni', 'Outdoor Adventure Specialist', '585-648-0667', 'mghioni26@camp.com', '29', '29'),
(80, 'Matt', 'Guerro', 'Outdoor Adventure Specialist', '585-648-0667', 'mguerni26@camp.com', '40', '40');

INSERT INTO Admin (adminID, firstName, lastName, email, phone) VALUES 
(1, 'Stephanie', 'Black', 'sblack@summersync.com', '230-255-0111'),
(2, 'Judas', 'Boraston', 'jboraston1@summersync.com', '554-357-8666'),
(3, 'Paulo', 'Cruddas', 'pcruddas2@summersync.com', '630-189-6718'),
(4, 'Niel', 'Hudson', 'nhudson3@summersync.com', '680-421-3935'),
(5, 'Paulie', 'Antosch', 'pantosch4@summersync.com', '297-184-4316'),
(6, 'Lela', 'Gullam', 'lgullam5@summersync.com', '680-752-9502'),
(7, 'Rolfe', 'Boddis', 'rboddis6@summersync.com', '593-958-9498'),
(8, 'Andee', 'Corriea', 'acorriea7@summersync.com', '280-204-9334'),
(9, 'Kaila', 'Peltz', 'kpeltz8@summersync.com', '823-632-9018'),
(10, 'Martica', 'Telling', 'mtelling9@summersync.com', '371-766-7299'),
(11, 'Joycelin', 'Pakes', 'jpakesa@summersync.com', '365-573-8170'),
(12, 'Charmion', 'Dwelly', 'cdwellyb@summersync.com', '263-941-7158'),
(13, 'Dania', 'Fletcher', 'dfletcherc@summersync.com', '595-868-8169'),
(14, 'Helaine', 'Dolby', 'hdolbyd@summersync.com', '836-335-2953'),
(15, 'Burtie', 'Kingsworth', 'bkingsworthe@summersync.com', '252-619-6694'),
(16, 'Gan', 'O''Mullally', 'gomullallyf@summersync.com', '435-182-9857'),
(17, 'Isiahi', 'Morgan', 'imorgang@summersync.com', '630-890-9271'),
(18, 'Morley', 'Matschoss', 'mmatschossh@summersync.com', '299-333-1230'),
(19, 'Tirrell', 'Gherardesci', 'tgherardescii@summersync.com', '114-450-3244'),
(20, 'Lanna', 'Lydster', 'llydsterj@summersync.com', '877-125-9059'),
(21, 'Ethel', 'Shapter', 'eshapterk@summersync.com', '956-598-9166'),
(22, 'Dannie', 'Joron', 'djoronl@summersync.com', '719-497-3743'),
(23, 'Chaunce', 'Bloxland', 'cbloxlandm@summersync.com', '641-210-7370'),
(24, 'Donella', 'Ensley', 'densleyn@summersync.com', '278-648-8718'),
(25, 'Twyla', 'Autry', 'tautryo@summersync.com', '287-137-3291'),
(26, 'Latisha', 'Tomaszynski', 'ltomaszynskip@summersync.com', '290-847-5493'),
(27, 'Elfrieda', 'MacGebenay', 'emacgebenayq@summersync.com', '881-134-9878'),
(28, 'Minor', 'Sackler', 'msacklerr@summersync.com', '596-438-2133'),
(29, 'Carrie', 'Chazelle', 'cchazelles@summersync.com', '315-923-0128'),
(30, 'Carroll', 'Ricardot', 'cricardott@summersync.com', '113-847-2421'),
(31, 'Iago', 'Latter', 'ilatteru@summersync.com', '733-763-6685'),
(32, 'Lammond', 'Tixall', 'ltixallv@summersync.com', '927-695-3433'),
(33, 'Kaja', 'Liggens', 'kliggensw@summersync.com', '559-326-6267'),
(34, 'Sharla', 'Douch', 'sdouchx@summersync.com', '670-979-8252'),
(35, 'Dorine', 'McPhate', 'dmcphatey@summersync.com', '782-577-6292'),
(36, 'Silvie', 'Woolhouse', 'swoolhousez@summersync.com', '583-175-2082'),
(37, 'Rozelle', 'Stallibrass', 'rstallibrass10@summersync.com', '122-330-6435'),
(38, 'Edmund', 'Hawkin', 'ehawkin11@summersync.com', '142-817-9544'),
(39, 'Homerus', 'Dufton', 'hdufton12@summersync.com', '262-835-1185'),
(40, 'Davin', 'Smalridge', 'dsmalridge13@summersync.com', '701-791-4377');

INSERT INTO Location (locationID, region, territory, adminID) VALUES 
(1, 'Minnesota', 'Minneapolis', '22'),
(2, 'Connecticut', 'New Haven', '32'),
(3, 'Florida', 'Homestead', '11'),
(4, 'Illinois', 'Chicago', '4'),
(5, 'Rhode Island', 'Providence', '23'),
(6, 'Georgia', 'Atlanta', '36'),
(7, 'Alabama', 'Montgomery', '24'),
(8, 'Texas', 'Houston', '17'),
(9, 'Virginia', 'Newport News', '25'),
(10, 'South Carolina', 'Beaufort', '5'),
(11, 'New York', 'Brooklyn', '18'),
(12, 'Pennsylvania', 'Harrisburg', '16'),
(13, 'Ohio', 'Akron', '3'),
(14, 'California', 'Fresno', '19'),
(15, 'Texas', 'Houston', '7'),
(16, 'Michigan', 'Saginaw', '30'),
(17, 'Alabama', 'Huntsville', '28'),
(18, 'Pennsylvania', 'New Castle', '8'),
(19, 'Ohio', 'Columbus', '10'),
(20, 'Minnesota', 'Minneapolis', '2'),
(21, 'Iowa', 'Des Moines', '38'),
(22, 'Washington', 'Vancouver', '29'),
(23, 'Missouri', 'Springfield', '33'),
(24, 'Missouri', 'Kansas City', '40'),
(25, 'Florida', 'Orlando', '15'),
(26, 'South Carolina', 'Columbia', '34'),
(27, 'Alabama', 'Birmingham', '1'),
(28, 'California', 'Los Angeles', '12'),
(29, 'Florida', 'Clearwater', '9'),
(30, 'Alabama', 'Birmingham', '6'),
(31, 'Pennsylvania', 'Reading', '26'),
(32, 'New Jersey', 'Paterson', '13'),
(33, 'Missouri', 'Columbia', '21'),
(34, 'New York', 'Brooklyn', '37'),
(35, 'Texas', 'Dallas', '14'),
(36, 'Pennsylvania', 'Pittsburgh', '27'),
(37, 'Ohio', 'Dayton', '31'),
(38, 'Georgia', 'Columbus', '35'),
(39, 'West Virginia', 'Morgantown', '20'),
(40, 'Massachusetts', 'New Bedford', '39');

INSERT INTO CampLoc (campID, locationID) VALUES
(1, 17), (2, 7), (3, 38), (4, 16), (5, 18),
(6, 22), (7, 13), (8, 29), (9, 24), (10, 40),
(11, 31), (12, 19), (13, 39), (14, 5), (15, 23),
(16, 34), (17, 14), (18, 3), (19, 26), (20, 15),
(21, 10), (22, 33), (23, 2), (24, 37), (25, 11),
(26, 6), (27, 12), (28, 25), (29, 27), (30, 1),
(31, 4), (32, 32), (33, 8), (34, 30), (35, 28),
(36, 20), (37, 9), (38, 21), (39, 36), (40, 35),
(1, 23), (2, 11), (3, 29), (4, 20), (5, 6),
(6, 7), (7, 22), (8, 24), (9, 34), (10, 32),
(11, 1), (12, 27), (13, 2), (14, 40), (15, 36),
(16, 39), (17, 35), (18, 33), (19, 15), (20, 12),
(21, 25), (22, 38), (23, 15), (24, 6), (25, 9),
(26, 33), (27, 24), (28, 30), (29, 31), (30, 3),
(31, 37), (32, 14), (33, 4), (34, 5), (35, 3),
(36, 26), (37, 13), (38, 6), (39, 28), (40, 5),
(1, 40), (2, 39), (3, 1), (4, 2), (5, 4),
(6, 8), (7, 10), (8, 12), (9, 14), (10, 16),
(11, 18), (12, 20), (13, 22), (14, 24), (15, 26),
(16, 28), (17, 30), (18, 32), (19, 34), (20, 36),
(21, 38), (22, 1), (23, 3), (24, 5), (25, 7),
(26, 9), (27, 11), (28, 13), (29, 15), (30, 17),
(31, 19), (32, 21), (33, 23), (34, 25), (35, 27),
(36, 29), (37, 31), (38, 33), (39, 35), (40, 37);

INSERT INTO MedicalInfo (medID, type) VALUES 
(1, 'Peanut allergy'),
(2, 'Tree nut allergy'),
(3, 'Dairy allergy'),
(4, 'Egg allergy'),
(5, 'Soy allergy'),
(6, 'Wheat allergy'),
(7, 'Shellfish allergy'),
(8, 'Fish allergy'),
(9, 'Gluten free/Celiac disease'),
(10, 'Sesame allergy'),
(11, 'Corn allergy'),
(12, 'Mustard allergy'),
(13, 'Lactose intolerance'),
(14, 'Vegan diet'),
(15, 'Vegetarian diet'),
(16, 'Halal diet'),
(17, 'Kosher diet'),
(18, 'Low-sodium diet'),
(19, 'Low-sugar/Diabetic diet'),
(20, 'High-protein diet'),
(21, 'FODMAP diet'),
(22, 'Keto diet'),
(23, 'Nut-free diet'),
(24, 'Asthma'),
(25, 'Type 1 Diabetes'),
(26, 'Epilepsy'),
(27, 'ADHD'),
(28, 'Autism Spectrum Disorder (ASD)'),
(29, 'Anxiety disorders'),
(30, 'Depression'),
(31, 'Cerebral palsy'),
(32, 'Down syndrome'),
(33, 'Hemophilia'),
(34, 'Juvenile rheumatoid arthritis'),
(35, 'Congenital heart defects'),
(36, 'Cystic fibrosis'),
(37, 'Sickle cell anemia'),
(38, 'Eczema'),
(39, 'FPIES'),
(40, 'Migraines');

INSERT INTO Cabin (cabinID, cabinName, staffID, capacity) VALUES 
(1, 'Red-billed buffalo weaver', '1', 6),
(2, 'Elephant, asian', '33', 6),
(3, 'Goliath heron', '40', 6),
(4, 'Blue-footed booby', '23', 8),
(5, 'Badger, american', '21', 10),
(6, 'Spotted wood sandpiper', '3', 10),
(7, 'Pied cormorant', '4', 8),
(8, 'Gull, swallow-tail', '22', 10),
(9, 'Kalahari scrub robin', '14', 10),
(10, 'Topi', '27', 6),
(11, 'Yellow-billed stork', '25', 6),
(12, 'Black-throated butcher bird', '19', 8),
(13, 'Ring-tailed lemur', '16', 10),
(14, 'Frogmouth, tawny', '20', 6),
(15, 'Australian brush turkey', '8', 10),
(16, 'White-headed vulture', '24', 10),
(17, 'Trumpeter, dark-winged', '9', 10),
(18, 'Tortoise, burmese brown mountain', '7', 8),
(19, 'Bushpig', '12', 8),
(20, 'Golden brush-tailed possum', '18', 10),
(21, 'Asian water buffalo', '35', 8),
(22, 'Grenadier, common', '32', 8),
(23, 'Stork, black-necked', '34', 6),
(24, 'Caracara (unidentified)', '31', 10),
(25, 'Insect, stick', '38', 6),
(26, 'Wagtail, african pied', '17', 10),
(27, 'Black-collared barbet', '15', 6),
(28, 'Squirrel, richardson''s ground', '37', 8),
(29, 'Gull, kelp', '13', 6),
(30, 'Squirrel, palm', '10', 8),
(31, 'Ant (unidentified)', '39', 6),
(32, 'Black-collared barbet', '30', 8),
(33, 'Dove, mourning collared', '11', 8),
(34, 'Brown capuchin', '6', 10),
(35, 'Mocking cliffchat', '28', 6),
(36, 'Bird (unidentified)', '36', 6),
(37, 'Goose, canada', '5', 8),
(38, 'Scaly-breasted lorikeet', '26', 10),
(39, 'Dragon, asian water', '2', 10),
(40, 'Woodrat (unidentified)', '29', 10);

INSERT INTO Bed (bedID, cabinID) VALUES
(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
(6, 6), (7, 7), (8, 8), (9, 9), (10, 10),
(11, 11), (12, 12), (13, 13), (14, 14), (15, 15),
(16, 16), (17, 17), (18, 18), (19, 19), (20, 20),
(21, 21), (22, 22), (23, 23), (24, 24), (25, 25),
(26, 26), (27, 27), (28, 28), (29, 29), (30, 30),
(31, 31), (32, 32), (33, 33), (34, 34), (35, 35),
(36, 36), (37, 37), (38, 38), (39, 39), (40, 40),
(41, 1), (42, 2), (43, 3), (44, 4), (45, 5),
(46, 6), (47, 7), (48, 8), (49, 9), (50, 10);

INSERT INTO Camper (camperID, firstName, lastName, campID, DOB, guardianID, bedID, cabinID, staffID) VALUES
(1, 'Alyda', 'Stodit', '21', '2011-08-20', '10', 4, 4, '28'),
(2, 'Flemming', 'Houldin', '2', '2014-09-27', '22', 7, 7, '1'),
(3, 'Mickie', 'Caen', '24', '2015-07-17', '20', 33, 33, '11'),
(4, 'Fifi', 'Shiell', '3', '2012-01-14', '24', 11, 11, '38'),
(5, 'Bentlee', 'Alford', '20', '2018-01-04', '3', 5, 5, '39'),
(6, 'Lidia', 'Caberas', '5', '2011-01-26', '25', 25, 25, '9'),
(7, 'Alikee', 'Raddenbury', '40', '2013-11-20', '17', 27, 27, '23'),
(8, 'Briana', 'Walbrun', '26', '2017-02-02', '22', 3, 3, '18'),
(9, 'Jemmy', 'Thelwll', '17', '2008-06-27', '12', 38, 38, '22'),
(10, 'Frieda', 'Carville', '31', '2014-12-01', '12', 34, 34, '19'),
(11, 'Douglas', 'Cobbing', '33', '2012-01-26', '22', 11, 11, '7'),
(12, 'Inna', 'Beckson', '36', '2011-04-21', '16', 4, 4, '12'),
(13, 'Ashely', 'Syddie', '38', '2011-11-28', '20', 26, 26, '2'),
(14, 'Stevana', 'Stapforth', '12', '2006-08-05', '14', 6, 6, '5'),
(15, 'Roze', 'Raccio', '14', '2010-08-18', '20', 32, 32, '3'),
(16, 'Arvy', 'Buscher', '35', '2006-07-25', '18', 9, 9, '16'),
(17, 'Obidiah', 'Faich', '34', '2014-11-17', '14', 36, 36, '17'),
(18, 'Clyve', 'Dormand', '37', '2017-02-08', '1', 40, 40, '8'),
(19, 'Verne', 'Obee', '39', '2008-02-18', '15', 28, 28, '35'),
(20, 'Andrea', 'Hertwell', '28', '2012-04-27', '1', 18, 18, '6'),
(21, 'Keven', 'Feild', '27', '2015-10-19', '22', 2, 2, '36'),
(22, 'Boot', 'Ocklin', '22', '2013-04-13', '9', 16, 16, '30'),
(23, 'Tine', 'Cordobes', '30', '2010-03-03', '12', 19, 19, '24'),
(24, 'Cherye', 'Carnew', '1', '2014-12-07', '4', 20, 20, '33'),
(25, 'Dyann', 'Tue', '4', '2016-05-29', '4', 30, 30, '31'),
(26, 'Cam', 'Blincko', '18', '2008-05-08', '1', 14, 14, '26'),
(27, 'Rufus', 'Sebert', '11', '2012-02-19', '4', 15, 15, '29'),
(28, 'Martelle', 'Gommey', '19', '2014-04-30', '8', 1, 1, '25'),
(29, 'Izaak', 'Moriarty', '7', '2018-04-21', '8', 23, 23, '13'),
(30, 'Yanaton', 'Biesty', '13', '2015-03-05', '6', 21, 21, '15'),
(31, 'Correy', 'Aleksankin', '23', '2006-09-02', '25', 31, 31, '27'),
(32, 'Cathyleen', 'O''Heaney', '6', '2008-08-04', '10', 12, 12, '34'),
(33, 'Orrin', 'Ganley', '29', '2011-12-19', '20', 29, 29, '32'),
(34, 'Cori', 'MacGaughy', '25', '2009-11-20', '23', 10, 10, '20'),
(35, 'Valdemar', 'Hazlegrove', '16', '2007-09-29', '21', 22, 22, '14'),
(36, 'Markos', 'Lacotte', '15', '2012-10-09', '4', 17, 17, '4'),
(37, 'Faye', 'Waple', '10', '2017-05-11', '2', 13, 13, '21'),
(38, 'Everard', 'Borham', '32', '2018-03-09', '9', 7, 7, '40'),
(39, 'Marvin', 'Vaney', '8', '2013-03-23', '8', 37, 37, '37'),
(40, 'Clementina', 'Osipenko', '9', '2016-12-15', '3', 24, 24, '10');

INSERT INTO MedNeeds (medID, camperID) VALUES 
('36', '13'), ('9', '19'), ('7', '15'), ('8', '26'), ('22', '29'),
('27', '18'), ('28', '33'), ('4', '6'), ('31', '9'), ('21', '14'),
('3', '1'), ('14', '20'), ('20', '17'), ('12', '27'), ('35', '2'),
('19', '3'), ('32', '23'), ('13', '31'), ('10', '16'), ('5', '7'),
('2', '30'), ('29', '28'), ('38', '11'), ('24', '39'), ('30', '5'),
('40', '32'), ('6', '25'), ('25', '38'), ('15', '40'), ('16', '8'),
('1', '37'), ('37', '4'), ('34', '21'), ('39', '35'), ('11', '10'),
('23', '22'), ('26', '36'), ('18', '24'), ('17', '12'), ('33', '34'),
('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6'),
('6', '7'), ('7', '8'), ('8', '9'), ('9', '10'), ('10', '11'),
('11', '12'), ('12', '13'), ('13', '14'), ('14', '15'), ('15', '16'),
('16', '17'), ('17', '18'), ('18', '19'), ('19', '20'), ('20', '21'),
('21', '22'), ('22', '23'), ('23', '24'), ('24', '25'), ('25', '26'),
('26', '27'), ('27', '28'), ('28', '29'), ('29', '30'), ('30', '31'),
('31', '32'), ('32', '33'), ('33', '35'), ('34', '36'), ('35', '37'),
('36', '38'), ('37', '39'), ('38', '40'), ('39', '1'), ('40', '2'),
('1', '3'), ('2', '4'), ('3', '5'), ('4', '7'), ('5', '8'),
('6', '9'), ('7', '10'), ('8', '11'), ('9', '12'), ('10', '13'),
('11', '14'), ('12', '15'), ('13', '16'), ('14', '17'), ('15', '18'),
('16', '19'), ('17', '20'), ('18', '21'), ('19', '22'), ('20', '23');

INSERT INTO DailySchedule (scheduleID, date, time, campID, sessionID) VALUES
(1, '2024-07-22', '19:19:00', '32', '32'),
(2, '2024-07-23', '10:55:00', '1', '1'),
(3, '2024-07-24', '19:57:00', '25', '25'),
(4, '2024-07-25', '18:25:00', '16', '16'),
(5, '2024-07-26', '14:57:00', '10', '10'),
(6, '2024-07-27', '09:19:00', '7', '7'),
(7, '2024-07-28', '23:12:00', '22', '22'),
(8, '2024-07-29', '14:48:00', '19', '19'),
(9, '2024-07-30', '13:07:00', '39', '39'),
(10, '2024-07-31', '08:57:00', '17', '17'),
(11, '2024-08-01', '08:53:00', '27', '27'),
(12, '2024-08-02', '08:49:00', '30', '30'),
(13, '2024-08-03', '15:20:00', '4', '4'),
(14, '2024-08-04', '16:44:00', '32', '32'),
(15, '2024-08-05', '15:52:00', '6', '6'),
(16, '2024-08-06', '21:40:00', '22', '22'),
(17, '2024-08-07', '21:24:00', '26', '26'),
(18, '2024-08-08', '14:53:00', '1', '1'),
(19, '2024-08-09', '23:39:00', '10', '10'),
(20, '2024-08-10', '13:42:00', '24', '24'),
(21, '2024-08-11', '13:04:00', '15', '15'),
(22, '2024-08-12', '18:43:00', '13', '13'),
(23, '2024-08-13', '10:18:00', '34', '34'),
(24, '2024-08-14', '12:28:00', '14', '14'),
(25, '2024-08-15', '21:18:00', '5', '5'),
(26, '2024-08-16', '22:25:00', '22', '22'),
(27, '2024-08-17', '20:18:00', '38', '38'),
(28, '2024-08-18', '21:45:00', '3', '3'),
(29, '2024-08-19', '22:10:00', '16', '16'),
(30, '2024-08-20', '12:46:00', '32', '32'),
(31, '2024-08-21', '12:19:00', '27', '27'),
(32, '2024-08-22', '16:35:00', '28', '28'),
(33, '2024-08-23', '11:38:00', '18', '18'),
(34, '2024-08-24', '08:30:00', '6', '6'),
(35, '2024-08-25', '23:33:00', '30', '30'),
(36, '2024-08-26', '14:53:00', '4', '4'),
(37, '2024-08-27', '22:37:00', '15', '15'),
(38, '2024-08-28', '13:08:00', '13', '13'),
(39, '2024-08-29', '22:25:00', '23', '23'),
(40, '2024-08-30', '21:20:00', '24', '24'),
(41, '2024-08-31', '20:00:00', '20', '20');

INSERT INTO Activity (activityID, name, description) VALUES 
(1, 'Hiking', 'Explore scenic trails and enjoy the beauty of nature while walking through various terrains.'),
(2, 'Archery', 'Learn the art of archery, focusing on technique and accuracy while shooting arrows at targets.'),
(3, 'Swimming', 'Enjoy refreshing swims in the pool or lake, with games and activities for all skill levels.'),
(4, 'Canoeing', 'Paddle through calm waters, learning basic canoeing skills and teamwork while enjoying the outdoors.'),
(5, 'Kayaking', 'Experience kayaking on the lake, navigating through gentle waters and enjoying the tranquility of nature.'),
(6, 'Rock climbing', 'Challenge yourself with rock climbing, focusing on safety, techniques, and conquering climbing walls.'),
(7, 'Zip-lining', 'Soar through the treetops on a zip-line, experiencing the thrill of flying while enjoying stunning views.'),
(8, 'Arts and crafts', 'Engage in creative projects using various materials to make unique crafts and artwork.'),
(9, 'Nature walks', 'Take guided walks to learn about local flora and fauna while enjoying the peacefulness of nature.'),
(10, 'Campfire storytelling', 'Gather around the campfire to share stories, legends, and experiences under the stars.'),
(11, 'Orienteering', 'Develop navigation skills using maps and compasses while exploring the outdoors in a fun challenge.'),
(12, 'Horseback riding', 'Experience horseback riding through trails, focusing on riding techniques and horse care.'),
(13, 'Fishing', 'Learn fishing techniques and enjoy a relaxing day by the water, catching fish and enjoying nature.'),
(14, 'Birdwatching', 'Discover local bird species while learning about their habitats and behaviors through guided observation.'),
(15, 'Soccer', 'Participate in soccer games, learning teamwork and skills while enjoying friendly competition.'),
(16, 'Scavenger hunts', 'Join in on scavenger hunts, searching for items and completing challenges in a fun, interactive way.'),
(17, 'Talent shows', 'Showcase your talents in a fun and supportive environment, encouraging creativity and performance skills.'),
(18, 'Outdoor cooking', 'Learn to cook delicious meals outdoors, focusing on campfire cooking techniques and food safety.'),
(19, 'Survival skills training', 'Gain essential survival skills, including shelter building, fire making, and foraging for food.'),
(20, 'Star gazing', 'Enjoy an evening of star gazing, learning about constellations and celestial events with telescopes.'),
(21, 'Dance parties', 'Join in on lively dance parties, featuring music and fun dance games for everyone to enjoy.'),
(22, 'Capture the flag', 'Participate in this classic outdoor game, focusing on teamwork and strategy to capture the flag of the opposing team.'),
(23, 'Relay races', 'Engage in fun relay races, promoting teamwork and friendly competition among campers.'),
(24, 'Yoga', 'Practice yoga in a serene outdoor setting, focusing on relaxation, flexibility, and mindfulness.'),
(25, 'Meditation', 'Learn meditation techniques to promote relaxation and mental clarity in a peaceful environment.'),
(26, 'Gardening', 'Get hands-on experience in gardening, learning about plant care, and growing your own vegetables and flowers.'),
(27, 'Environmental education', 'Participate in activities that teach about sustainability, conservation, and the importance of protecting nature.'),
(28, 'Drama/Improv games', 'Engage in fun drama and improv games to boost creativity and confidence in performance arts.'),
(29, 'Music workshops', 'Participate in music workshops, exploring different instruments and learning to create music together.'),
(30, 'Photography', 'Learn photography skills, capturing the beauty of nature and camp activities through your lens.'),
(31, 'Pottery', 'Get creative with pottery, learning techniques to shape and glaze your own unique pieces.'),
(32, 'Mountain biking', 'Experience the thrill of mountain biking on trails, focusing on safety and riding techniques.'),
(33, 'High ropes course', 'Challenge yourself on a high ropes course, building confidence and teamwork while navigating obstacles.'),
(34, 'Low ropes course', 'Work together on a low ropes course, focusing on teamwork and communication in a fun environment.'),
(35, 'Sailing', 'Learn the basics of sailing, focusing on navigation, teamwork, and enjoying the open water.'),
(36, 'Paddleboarding', 'Experience paddleboarding on calm waters, enhancing balance and enjoying the serenity of the lake.'),
(37, 'Slip and slide', 'Have fun on a slip and slide, enjoying a refreshing and exciting way to cool off on hot days.'),
(38, 'Campout under the stars', 'Enjoy a night camping outdoors, learning about nature and sharing stories around the campfire.'),
(39, 'Tie-dyeing', 'Get creative with tie-dyeing, making colorful and unique clothing and accessories.'),
(40, 'Animal tracking', 'Learn to identify animal tracks and signs in nature, enhancing your observation skills while exploring.'); 

INSERT INTO RequiredItems (requiredItems, activityID) VALUES 
('Walking stick', '32'),
('Sunglasses, sunscreen, and hat', '1'),
('Playing cards and board game', '26'),
('Laundry bag and detergent', '10'),
('Binoculars and bird guide', '4'),
('Firewood and matches', '31'),
('Travel pillow and eye mask', '18'),
('Hiking boots', '19'),
('Firewood and matches', '21'),
('Binoculars and bird guide', '12'),
('Folding chair', '39'),
('Flashlights', '29'),
('First aid kit', '38'),
('Tent, sleeping bag, and mat', '5'),
('Helmet and gloves', '40'),
('S''mores ingredients', '27'),
('First aid kit', '20'),
('Hand sanitizer and wipes', '9'),
('First aid kit', '36'),
('Portable charger', '30'),
('Marshmallows', '34'),
('Yoga mat', '11'),
('Yoga mat', '35'),
('Rope, carabiner, and harness', '22'),
('Art supplies and sketchpad', '6'),
('Bug spray', '13'),
('Portable grill and charcoal', '16'),
('Hiking boots', '7'),
('Binoculars and bird guide', '24'),
('Travel pillow and eye mask', '23'),
('S''mores ingredients', '25'),
('Laundry bag and detergent', '3'),
('Lantern and fuel', '28'),
('Sunscreen and fishing rods', '33'),
('Swimsuit and towel', '14'),
('Portable charger', '17'),
('Folding chair', '15'),
('Picnic blanket and basket', '37'),
('Walking stick', '2'),
('Art supplies and sketchpad', '8');

INSERT INTO ScheduleActivity (activityID, scheduleID) VALUES
('23', '28'), ('25', '18'), ('12', '31'), ('2', '4'), ('8', '35'),
('3', '15'), ('31', '19'), ('36', '39'), ('34', '37'), ('14', '40'),
('1', '1'), ('15', '24'), ('22', '14'), ('9', '21'), ('29', '34'),
('6', '32'), ('5', '3'), ('16', '34'), ('19', '36'), ('21', '10'),
('18', '29'), ('11', '11'), ('33', '9'), ('13', '23'), ('32', '26'),
('20', '5'), ('40', '30'), ('35', '20'), ('30', '6'), ('17', '17'),
('4', '7'), ('26', '27'), ('28', '12'), ('7', '22'), ('37', '38'),
('39', '13'), ('38', '25'), ('24', '16'), ('27', '2'), ('10', '8'),
('1', '2'), ('2', '1'), ('3', '4'), ('4', '3'), ('5', '6'),
('6', '5'), ('7', '8'), ('8', '7'), ('9', '10'), ('10', '9'),
('11', '12'), ('12', '11'), ('13', '14'), ('14', '13'), ('15', '16'),
('16', '15'), ('17', '18'), ('18', '17'), ('19', '20'), ('20', '19'),
('21', '22'), ('22', '21'), ('23', '24'), ('24', '23'), ('25', '26'),
('26', '25'), ('27', '28'), ('28', '27'), ('29', '30'), ('30', '29'),
('31', '32'), ('32', '31'), ('33', '34'), ('34', '33'), ('35', '36'),
('36', '35'), ('37', '39'), ('38', '37'), ('39', '40'), ('40', '39'),
('1', '3'), ('2', '5'), ('3', '7'), ('4', '9'), ('5', '11'),
('6', '13'), ('7', '15'), ('8', '17'), ('9', '19'), ('10', '21'),
('11', '23'), ('12', '25'), ('13', '27'), ('14', '29'), ('15', '31'),
('16', '33'), ('17', '35'), ('18', '37'), ('19', '39'), ('20', '1')


