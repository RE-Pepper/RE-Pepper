

# File alFileLoader.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**File**](dir_434e756ae3930eedc6101a4f10d5330c.md) **>** [**alFileLoader.h**](al_file_loader_8h.md)

[Go to the documentation of this file](al_file_loader_8h.md)


```C++
#pragma once

#include <prim/seadSafeString.h>

namespace sead
{
class FileDevice;
}

namespace al
{

class FileLoader
{
private:
        u8 _0[ 0x30 ];

public:
        void loadArchive( const sead::SafeString& archive, sead::FileDevice* );

public:
        FileLoader( int );
};

} // namespace al
```


