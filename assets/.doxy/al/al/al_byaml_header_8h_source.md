

# File alByamlHeader.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Yaml**](dir_ead735227c22214cb122acbd07613fdc.md) **>** [**alByamlHeader.h**](al_byaml_header_8h.md)

[Go to the documentation of this file](al_byaml_header_8h.md)


```C++
#pragma once

namespace al
{

#pragma diag_suppress 368 // struct only for reading data

class ByamlHeader
{
private:
        const u16 mTag;
        const u16 mVersion;
        const int mHashKeyOffset;
        const int mStringTableOffset;
        const int mDataOffset;

public:
        u16 getTag() const
        {
                return mTag;
        }

        u16 getVersion() const
        {
                return mVersion;
        }

        u32 getHashKeyTableOffset() const
        {
                return mHashKeyOffset;
        }

        u32 getStringTableOffset() const
        {
                return mStringTableOffset;
        };

        u32 getDataOffset() const
        {
                return mDataOffset;
        };
};

} // namespace al

namespace alByamlLocalUtil
{

bool verifiByaml( const u8* data );

} // namespace alByamlLocalUtil
```


