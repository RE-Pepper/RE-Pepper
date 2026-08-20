#pragma once

#include <math/seadMatrix.h>

class alModelCtr;

namespace al
{

class ModelKeeper
{
private:
        alModelCtr* mModel;

public:
        alModelCtr* getModel() const
        {
                return mModel;
        }

        void hide();
};

const sead::Matrix34f* getJointMtxPtr( ModelKeeper* keeper, const char* jointName );

} // namespace al
