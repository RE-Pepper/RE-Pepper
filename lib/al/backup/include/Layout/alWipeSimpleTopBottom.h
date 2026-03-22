#pragma once

namespace al
{

class WipeSimple;

class WipeSimpleTopBottom
{
private:
        WipeSimple* mTop;
        WipeSimple* mBottom;

public:
        inline WipeSimple* getTop() const
        {
                return mTop;
        }

        inline WipeSimple* getBottom() const
        {
                return mBottom;
        }

        bool isCloseEnd() const;

public:
        WipeSimpleTopBottom( const char* name, const char* archive, const char*, const LayoutInitInfo& info, const char* subArchive );
};

} // namespace al
