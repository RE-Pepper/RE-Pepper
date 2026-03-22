#pragma once

class CourseList;

class GameDataFile
{
private:
        u8   _0[ 0x44 ];
        bool mIs3DOn;

public:
        GameDataFile( CourseList* courseList );
};
