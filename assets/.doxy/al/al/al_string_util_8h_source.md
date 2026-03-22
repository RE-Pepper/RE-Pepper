

# File alStringUtil.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Util**](dir_38a3d91dc6c502fa895bc5833df868a6.md) **>** [**alStringUtil.h**](al_string_util_8h.md)

[Go to the documentation of this file](al_string_util_8h.md)


```C++
#pragma once

// Temporary file because I can't figure out what the folder is (al/A____ or al/B____)
// please replace

#include <prim/seadSafeString.h>

namespace al
{

template <s32 L>
class StringTmp : public sead::FixedSafeString<L>
{
public:
        StringTmp( const char* format, ... ) : sead::FixedSafeString<L>()
        {
                va_list args;
                va_start( args, format );
                this->formatV( format, args );
                va_end( args );
        }
};

const char* getBaseName( const char* name );
const char* createStringIfInStack( const char* str );
bool        isEqualString( const char* s1, const char* s2 );
bool        isEqualString( const sead::SafeString& s1, const sead::SafeString& s2 );
bool        isEqualSubString( const char* str, const char* substr );
bool        isInStack( const void* ptr );

} // namespace al
```


