#pragma once

class CourseList;

class SaveDataFile
{
private:
        u8  _0[ 0x3e ];
        u16 mNumLife;
        u16 mNumCoinCollect;
        u8  _42[ 0x1a ];

public:
        void initializeData( CourseList* courseList );

public:
        SaveDataFile();
};
