

# File alByamlContainerHeader.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Yaml**](dir_ead735227c22214cb122acbd07613fdc.md) **>** [**alByamlContainerHeader.h**](al_byaml_container_header_8h.md)

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


