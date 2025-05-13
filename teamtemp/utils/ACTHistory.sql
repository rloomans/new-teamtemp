DELETE FROM responses_teamresponsehistory where request_id = 'ACT00000';
DELETE FROM responses_teams where request_id = 'ACT00000';
DELETE FROM responses_temperatureresponse where request_id = 'ACT00000';
DELETE FROM responses_teamtemperature where id = 'ACT00000';
DELETE FROM responses_user where id = 'ACTUSER0';


INSERT INTO responses_user (id) VALUES ('ACTUSER0');

INSERT INTO responses_teamtemperature (id, creation_date, creator_id, password) VALUES ('ACT00000', '2014-04-29', 'ACTUSER0', 'bcrypt$$2a$12$FG5Ok0J22BD1Nz8M4kS8F.S3pAbbaUMKw1weHiy9MNEsazzjv/F8G');

INSERT INTO responses_teamresponsehistory (request_id, average_score, word_list, responder_count, team_name, archive_date) VALUES ('ACT00000', 6.40000, '', 14, 'Transaction_and_Payment_Mgmt', '2014-04-29 01:58:24.013317+10');
INSERT INTO responses_teamresponsehistory (request_id, average_score, word_list, responder_count, team_name, archive_date) VALUES ('ACT00000', 6.00000, '', 5, 'Transaction_and_Payment_Mgmt', '2014-05-13 01:58:24.013317+10');
INSERT INTO responses_teamresponsehistory (request_id, average_score, word_list, responder_count, team_name, archive_date) VALUES ('ACT00000', 5.50000, '', 9, 'Transaction_and_Payment_Mgmt', '2014-05-27 01:58:24.013317+10');
INSERT INTO responses_teamresponsehistory (request_id, average_score, word_list, responder_count, team_name, archive_date) VALUES ('ACT00000', 6.60000, '', 10, 'Transaction_and_Payment_Mgmt', '2014-06-10 01:58:24.013317+10');

INSERT INTO responses_teamresponsehistory (request_id, average_score, word_list, responder_count, team_name, archive_date) VALUES ('ACT00000', 4.30000, '', 3, 'Card_Management', '2014-04-29 01:58:24.013317+10');
INSERT INTO responses_teamresponsehistory (request_id, average_score, word_list, responder_count, team_name, archive_date) VALUES ('ACT00000', 5.75000, '', 4, 'Card_Management', '2014-05-13 01:58:24.013317+10');
INSERT INTO responses_teamresponsehistory (request_id, average_score, word_list, responder_count, team_name, archive_date) VALUES ('ACT00000', 7.00000, '', 3, 'Card_Management', '2014-05-27 01:58:24.013317+10');
INSERT INTO responses_teamresponsehistory (request_id, average_score, word_list, responder_count, team_name, archive_date) VALUES ('ACT00000', 7.30000, '', 3, 'Card_Management', '2014-06-10 01:58:24.013317+10');

INSERT INTO responses_teamresponsehistory (request_id, average_score, word_list, responder_count, team_name, archive_date) VALUES ('ACT00000', 5.50000, '', 4, 'Account_Management', '2014-04-29 01:58:24.013317+10');
INSERT INTO responses_teamresponsehistory (request_id, average_score, word_list, responder_count, team_name, archive_date) VALUES ('ACT00000', 5.75000, '', 4, 'Account_Management', '2014-05-13 01:58:24.013317+10');
INSERT INTO responses_teamresponsehistory (request_id, average_score, word_list, responder_count, team_name, archive_date) VALUES ('ACT00000', 7.20000, '', 5, 'Account_Management', '2014-05-27 01:58:24.013317+10');
INSERT INTO responses_teamresponsehistory (request_id, average_score, word_list, responder_count, team_name, archive_date) VALUES ('ACT00000', 7.00000, '', 5, 'Account_Management', '2014-06-10 01:58:24.013317+10');

INSERT INTO responses_teamresponsehistory (request_id, average_score, word_list, responder_count, team_name, archive_date) VALUES ('ACT00000', 5.90000, '', 0, 'Average', '2014-04-29 01:58:24.013317+10');
INSERT INTO responses_teamresponsehistory (request_id, average_score, word_list, responder_count, team_name, archive_date) VALUES ('ACT00000', 5.80000, '', 0, 'Average', '2014-05-13 01:58:24.013317+10');
INSERT INTO responses_teamresponsehistory (request_id, average_score, word_list, responder_count, team_name, archive_date) VALUES ('ACT00000', 6.30000, '', 0, 'Average', '2014-05-27 01:58:24.013317+10');
INSERT INTO responses_teamresponsehistory (request_id, average_score, word_list, responder_count, team_name, archive_date) VALUES ('ACT00000', 6.80000, '', 0, 'Average', '2014-06-10 01:58:24.013317+10');

INSERT INTO responses_teams (request_id,team_name) VALUES ('ACT00000', 'Transaction_and_Payment_Mgmt');
INSERT INTO responses_teams (request_id,team_name) VALUES ('ACT00000', 'Card_Management');
INSERT INTO responses_teams (request_id,team_name) VALUES ('ACT00000', 'Account_Management');
