/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | foam-extend: Open Source CFD
   \\    /   O peration     | Version:     4.1
    \\  /    A nd           | Web:         http://www.foam-extend.org
     \\/     M anipulation  | For copyright notice see file Copyright
-------------------------------------------------------------------------------
License
    This file is part of foam-extend.

    foam-extend is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or (at your
    option) any later version.

    foam-extend is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with foam-extend.  If not, see <http://www.gnu.org/licenses/>.

\*---------------------------------------------------------------------------*/

#include "functionObjectTemplate.H"
#include "functionObject.H"
#include "foamTime.H"
#include "fvCFD.H"
#include "unitConversion.H"

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{

// * * * * * * * * * * * * * * Static Data Members * * * * * * * * * * * * * //

defineTypeNameAndDebug(DataSummaryFunctionObject, 0);


// * * * * * * * * * * * * * * * Local Functions * * * * * * * * * * * * * * //

//{{{ begin localCode

//}}} end localCode


// * * * * * * * * * * * * * Private Member Functions  * * * * * * * * * * * //

const objectRegistry& DataSummaryFunctionObject::obr() const
{
    return obr_;
}


const fvMesh& DataSummaryFunctionObject::mesh() const
{
    return refCast<const fvMesh>(obr_);
}


// * * * * * * * * * * * * * * * * Constructors  * * * * * * * * * * * * * * //

DataSummaryFunctionObject::DataSummaryFunctionObject
(
    const word& name,
    const objectRegistry& obr,
    const dictionary& dict,
    const bool
)
:
    name_(name),
    obr_(obr)
{
    read(dict);
}


// * * * * * * * * * * * * * * * * Destructor  * * * * * * * * * * * * * * * //

DataSummaryFunctionObject::~DataSummaryFunctionObject()
{}


// * * * * * * * * * * * * * * * Member Functions  * * * * * * * * * * * * * //

void DataSummaryFunctionObject::read(const dictionary& dict)
{
    if (false)
    {
        Info<<"read DataSummary sha1: e42ae47cd5921c64fa8b2214f040ee9f8b04c7c0\n";
    }

//{{{ begin code
    
//}}} end code
}


void DataSummaryFunctionObject::execute()
{
    if (false)
    {
        Info<<"execute DataSummary sha1: e42ae47cd5921c64fa8b2214f040ee9f8b04c7c0\n";
    }

//{{{ begin code
    
//}}} end code
}


void DataSummaryFunctionObject::end()
{
    if (false)
    {
        Info<<"end DataSummary sha1: e42ae47cd5921c64fa8b2214f040ee9f8b04c7c0\n";
    }

//{{{ begin code
    
//}}} end code
}


void DataSummaryFunctionObject::timeSet()
{
    if (false)
    {
        Info<<"timeSet DataSummary sha1: e42ae47cd5921c64fa8b2214f040ee9f8b04c7c0\n";
    }

//{{{ begin codeTime
    
//}}} end code
}


void DataSummaryFunctionObject::write()
{
    if (false)
    {
        Info<<"write DataSummary sha1: e42ae47cd5921c64fa8b2214f040ee9f8b04c7c0\n";
    }

//{{{ begin code
    #line 75 "::DataSummary"
scalar t = mesh().time().value();

			const volScalarField& alpha1 = mesh().lookupObject<volScalarField>("alpha1");

            const volScalarField& p = mesh().lookupObject<volScalarField>("p");

			const volVectorField& U = mesh().lookupObject<volVectorField>("U");

            scalar vol = gSum(mesh().V());
            scalar Umax = max(mag(U.internalField()));
            scalar Umin = min(mag(U.internalField()));
            scalar Uave = fvc::domainIntegrate(mag(U)).value()/vol;
            scalar Mtot = fvc::domainIntegrate(alpha1).value()/vol;
            scalar pMax = max(p.internalField());
            scalar pMin = min(p.internalField());
            scalar pDiff = pMax - pMin;

			if( Pstream::master() == true )
			{
				std::ofstream fs;
				fs.open ("DataSummary.csv", std::fstream::app);
				fs.precision(8);
//				fs << t << "\t" << dt << "\t" << Q_pcInt << "\t" << V_Vapor << "\t" << Uy_Vapor << "\n" ;
                fs  << t << ", " << Uave  << ", " << Umax << ", "
                    << Umin << ", " << Mtot << ", " << pMax
                    << ", " << pMin << ", " << pDiff << "\n"  ;
				fs.close();
			}
//}}} end code
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

} // End namespace Foam


// ************************************************************************* //

