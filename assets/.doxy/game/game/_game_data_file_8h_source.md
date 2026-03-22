

# File GameDataFile.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**System**](dir_e1006d71d276319c0715d176f1f44d04.md) **>** [**GameDataFile.h**](_game_data_file_8h.md)

[Go to the documentation of this file](_game_data_file_8h.md)


```C++
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
```


