

# File alByamlContainerHeader.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Yaml**](dir_4db20b6947036956387e84dab645aa7e.md) **>** [**alByamlContainerHeader.h**](al_byaml_container_header_8h.md)

[Go to the documentation of this file](al_byaml_container_header_8h.md)


```C++
#pragma once

#include <Yaml/alByamlData.h>

namespace al
{

class ByamlContainerHeader
{
private:
        // ByamlDataType mType : 1;
        // u32 mSize : 3;
        union
        {
                u32 mSize;
                u8  mType;
        };

public:
        inline ByamlDataType getType() const
        {
                return (ByamlDataType)mType;
        }

        inline u32 getCount() const
        {
                return mSize >> 8;
        } // get last 3 bytes
};

} // namespace al
```


