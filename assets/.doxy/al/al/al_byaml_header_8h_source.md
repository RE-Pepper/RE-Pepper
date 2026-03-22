

# File alByamlHeader.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Yaml**](dir_4db20b6947036956387e84dab645aa7e.md) **>** [**alByamlHeader.h**](al_byaml_header_8h.md)

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


