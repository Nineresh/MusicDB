# README
## Why
I'm making this to learn and improve knowledge about Python programming, how to use Git, resources surrounding Git, database management, data structuring and project management.
## Project
MusicDB is a personal project to manage a music mp3 library. 
### Resources
+ [[SQLite]] datebase
+ eyed3 library
+ OS library
## Working on next..

### Set up menu for functions
like; create table, run populate program, 
### Add path to table
Add folder path to the music. (?)
### Implement a compare program for backup
A backup is stored on a external drive. In the program it should run a
populate code like 1.0 on both directories then compare if there are discrepancys between the two directories. Or run one sides compares to validate, without polutation code.

# SQLite Structure
One database with one table
Table [tracks]:
+ id
+ track
+ album
+ artist
+ year

## SQLite statement
CREATE TABLE "tracks" (
	"id"	INTEGER,
	"title"	TEXT,
	"album"	TEXT,
	"artist"	TEXT,
	"year"	INTERGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);