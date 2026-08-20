#pragma once

#include <math/seadMatrix.h>
#include <math/seadVector.h>

namespace al
{

class AreaShape
{
private:
        const sead::Matrix34f* mBaseMtxPtr;
        sead::Vector3f         mScale;

public:
        bool calcLocalPos( sead::Vector3f* out, const sead::Vector3f& trans ) const;

        void setBaseMtxPtr( const sead::Matrix34f* baseMtxPtr )
        {
                mBaseMtxPtr = baseMtxPtr;
        }

        void setScale( const sead::Vector3f& scale );

public:
        virtual bool isInVolume( const sead::Vector3f& trans ) const = 0;
        virtual void v1()                                            = 0;
        virtual void v2()                                            = 0;

public:
        AreaShape();
};

} // namespace al
