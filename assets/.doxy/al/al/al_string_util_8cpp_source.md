

# File alStringUtil.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Util**](dir_4478c2a5592b6f930f15f50e4557300c.md) **>** [**alStringUtil.cpp**](al_string_util_8cpp.md)

[Go to the documentation of this file](al_string_util_8cpp.md)


```C++
#include <Util/alStringUtil.h>
#include <cstdio>
#include <cstring>

namespace al
{

const char* getBaseName( const char* name )
{
        const char* baseName = std::strrchr( name, '/' );
        return !baseName ? name : baseName + 1;
}

const char* createStringIfInStack( const char* str )
{
        if ( isInStack( str ) )
        {
                std::size_t size      = std::strlen( str ) + 1;
                char*       newString = new char[ size ];
                std::snprintf( newString, size, "%s", str );
                return newString;
        }
        return str;
}

bool isEqualString( const char* s1, const char* s2 )
{
        char val2 = *s2++, val1 = *s1++;
        while ( val1 == val2 )
        {
                if ( val1 == '\0' )
                        return true;
                val1 = *s1++;
                val2 = *s2++;
        }
        return false;
}

#ifdef NON_MATCHING
bool isEqualString( const sead::SafeString& s1, const sead::SafeString& s2 )
{
        return isEqualString( s1.cstr(), s2.cstr() );
}
#endif

bool isEqualSubString( const char* str, const char* substr )
{
        return std::strstr( str, substr ) != nullptr;
}

char* removeExtensionString( char* res, size_t size, const char* str )
{
        std::snprintf( res, size, "%s", str );
        char* token1 = std::strrchr( res, '.' );
        char* token2 = std::strrchr( res, '/' );
        if ( token2 > token1 || ++token2 == token1 || !token1 )
                return token2;
        token2  = 0;
        *token1 = 0;
        return token2;
}

} // namespace al
```


