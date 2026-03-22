

# File alFileLoader.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**File**](dir_a1283b388f36cc77f3502fde80df9d33.md) **>** [**alFileLoader.h**](al_file_loader_8h.md)

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


