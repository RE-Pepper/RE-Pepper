

# File FileInfo.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Layout**](dir_1e009ca70b4067525ad05e79ab8e6ed1.md) **>** [**FileInfo.h**](_file_info_8h.md)

[Go to the documentation of this file](_file_info_8h.md)


```C++
#pragma once

#include <Layout/alLayoutActor.h>

class FileInfo : public al::LayoutActor
{
private:
        class FileSelect* mFileSelect;
        int               _34;
        int               _38;
        int               _3C;
        bool              _40;
        void*             _44;
        bool              _48;

public:
        virtual void appear();

public:
        FileInfo( const al::LayoutInitInfo& info, FileSelect* fileSelect );
};
```


