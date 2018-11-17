//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, v2.2.4 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2018.10.22 at 06:47:31 PM PDT 
//


package com.microsoft.Malmo.Schemas;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;


/**
 * <p>Java class for anonymous complex type.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * 
 * <pre>
 * &lt;complexType>
 *   &lt;complexContent>
 *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *       &lt;sequence>
 *         &lt;choice>
 *           &lt;element name="Parametric">
 *             &lt;complexType>
 *               &lt;complexContent>
 *                 &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                   &lt;all>
 *                     &lt;element name="x" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                     &lt;element name="y" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                     &lt;element name="z" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;/all>
 *                   &lt;attribute name="seed">
 *                     &lt;simpleType>
 *                       &lt;restriction base="{http://www.w3.org/2001/XMLSchema}string">
 *                         &lt;pattern value="random|[0-9]+"/>
 *                       &lt;/restriction>
 *                     &lt;/simpleType>
 *                   &lt;/attribute>
 *                 &lt;/restriction>
 *               &lt;/complexContent>
 *             &lt;/complexType>
 *           &lt;/element>
 *           &lt;element name="Linear">
 *             &lt;complexType>
 *               &lt;complexContent>
 *                 &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                   &lt;all>
 *                     &lt;element name="CanvasBounds" type="{http://ProjectMalmo.microsoft.com}UnnamedGridDefinition"/>
 *                     &lt;element name="InitialPos" type="{http://ProjectMalmo.microsoft.com}Pos"/>
 *                     &lt;element name="InitialVelocity" type="{http://ProjectMalmo.microsoft.com}Pos"/>
 *                   &lt;/all>
 *                 &lt;/restriction>
 *               &lt;/complexContent>
 *             &lt;/complexType>
 *           &lt;/element>
 *         &lt;/choice>
 *         &lt;element ref="{http://ProjectMalmo.microsoft.com}DrawingDecorator"/>
 *       &lt;/sequence>
 *       &lt;attribute name="ticksPerUpdate" type="{http://www.w3.org/2001/XMLSchema}int" default="1" />
 *     &lt;/restriction>
 *   &lt;/complexContent>
 * &lt;/complexType>
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {
    "parametric",
    "linear",
    "drawingDecorator"
})
@XmlRootElement(name = "AnimationDecorator")
public class AnimationDecorator {

    @XmlElement(name = "Parametric")
    protected AnimationDecorator.Parametric parametric;
    @XmlElement(name = "Linear")
    protected AnimationDecorator.Linear linear;
    @XmlElement(name = "DrawingDecorator", required = true)
    protected DrawingDecorator drawingDecorator;
    @XmlAttribute(name = "ticksPerUpdate")
    protected Integer ticksPerUpdate;

    /**
     * Gets the value of the parametric property.
     * 
     * @return
     *     possible object is
     *     {@link AnimationDecorator.Parametric }
     *     
     */
    public AnimationDecorator.Parametric getParametric() {
        return parametric;
    }

    /**
     * Sets the value of the parametric property.
     * 
     * @param value
     *     allowed object is
     *     {@link AnimationDecorator.Parametric }
     *     
     */
    public void setParametric(AnimationDecorator.Parametric value) {
        this.parametric = value;
    }

    /**
     * Gets the value of the linear property.
     * 
     * @return
     *     possible object is
     *     {@link AnimationDecorator.Linear }
     *     
     */
    public AnimationDecorator.Linear getLinear() {
        return linear;
    }

    /**
     * Sets the value of the linear property.
     * 
     * @param value
     *     allowed object is
     *     {@link AnimationDecorator.Linear }
     *     
     */
    public void setLinear(AnimationDecorator.Linear value) {
        this.linear = value;
    }

    /**
     * 
     *                 Define the drawing, relative to (0,0,0), which will be drawn for each frame of the animation.
     *             
     * 
     * @return
     *     possible object is
     *     {@link DrawingDecorator }
     *     
     */
    public DrawingDecorator getDrawingDecorator() {
        return drawingDecorator;
    }

    /**
     * Sets the value of the drawingDecorator property.
     * 
     * @param value
     *     allowed object is
     *     {@link DrawingDecorator }
     *     
     */
    public void setDrawingDecorator(DrawingDecorator value) {
        this.drawingDecorator = value;
    }

    /**
     * Gets the value of the ticksPerUpdate property.
     * 
     * @return
     *     possible object is
     *     {@link Integer }
     *     
     */
    public int getTicksPerUpdate() {
        if (ticksPerUpdate == null) {
            return  1;
        } else {
            return ticksPerUpdate;
        }
    }

    /**
     * Sets the value of the ticksPerUpdate property.
     * 
     * @param value
     *     allowed object is
     *     {@link Integer }
     *     
     */
    public void setTicksPerUpdate(Integer value) {
        this.ticksPerUpdate = value;
    }


    /**
     * <p>Java class for anonymous complex type.
     * 
     * <p>The following schema fragment specifies the expected content contained within this class.
     * 
     * <pre>
     * &lt;complexType>
     *   &lt;complexContent>
     *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
     *       &lt;all>
     *         &lt;element name="CanvasBounds" type="{http://ProjectMalmo.microsoft.com}UnnamedGridDefinition"/>
     *         &lt;element name="InitialPos" type="{http://ProjectMalmo.microsoft.com}Pos"/>
     *         &lt;element name="InitialVelocity" type="{http://ProjectMalmo.microsoft.com}Pos"/>
     *       &lt;/all>
     *     &lt;/restriction>
     *   &lt;/complexContent>
     * &lt;/complexType>
     * </pre>
     * 
     * 
     */
    @XmlAccessorType(XmlAccessType.FIELD)
    @XmlType(name = "", propOrder = {

    })
    public static class Linear {

        @XmlElement(name = "CanvasBounds", required = true)
        protected UnnamedGridDefinition canvasBounds;
        @XmlElement(name = "InitialPos", required = true)
        protected Pos initialPos;
        @XmlElement(name = "InitialVelocity", required = true)
        protected Pos initialVelocity;

        /**
         * Gets the value of the canvasBounds property.
         * 
         * @return
         *     possible object is
         *     {@link UnnamedGridDefinition }
         *     
         */
        public UnnamedGridDefinition getCanvasBounds() {
            return canvasBounds;
        }

        /**
         * Sets the value of the canvasBounds property.
         * 
         * @param value
         *     allowed object is
         *     {@link UnnamedGridDefinition }
         *     
         */
        public void setCanvasBounds(UnnamedGridDefinition value) {
            this.canvasBounds = value;
        }

        /**
         * Gets the value of the initialPos property.
         * 
         * @return
         *     possible object is
         *     {@link Pos }
         *     
         */
        public Pos getInitialPos() {
            return initialPos;
        }

        /**
         * Sets the value of the initialPos property.
         * 
         * @param value
         *     allowed object is
         *     {@link Pos }
         *     
         */
        public void setInitialPos(Pos value) {
            this.initialPos = value;
        }

        /**
         * Gets the value of the initialVelocity property.
         * 
         * @return
         *     possible object is
         *     {@link Pos }
         *     
         */
        public Pos getInitialVelocity() {
            return initialVelocity;
        }

        /**
         * Sets the value of the initialVelocity property.
         * 
         * @param value
         *     allowed object is
         *     {@link Pos }
         *     
         */
        public void setInitialVelocity(Pos value) {
            this.initialVelocity = value;
        }

    }


    /**
     * <p>Java class for anonymous complex type.
     * 
     * <p>The following schema fragment specifies the expected content contained within this class.
     * 
     * <pre>
     * &lt;complexType>
     *   &lt;complexContent>
     *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
     *       &lt;all>
     *         &lt;element name="x" type="{http://www.w3.org/2001/XMLSchema}string"/>
     *         &lt;element name="y" type="{http://www.w3.org/2001/XMLSchema}string"/>
     *         &lt;element name="z" type="{http://www.w3.org/2001/XMLSchema}string"/>
     *       &lt;/all>
     *       &lt;attribute name="seed">
     *         &lt;simpleType>
     *           &lt;restriction base="{http://www.w3.org/2001/XMLSchema}string">
     *             &lt;pattern value="random|[0-9]+"/>
     *           &lt;/restriction>
     *         &lt;/simpleType>
     *       &lt;/attribute>
     *     &lt;/restriction>
     *   &lt;/complexContent>
     * &lt;/complexType>
     * </pre>
     * 
     * 
     */
    @XmlAccessorType(XmlAccessType.FIELD)
    @XmlType(name = "", propOrder = {

    })
    public static class Parametric {

        @XmlElement(required = true)
        protected String x;
        @XmlElement(required = true)
        protected String y;
        @XmlElement(required = true)
        protected String z;
        @XmlAttribute(name = "seed")
        protected String seed;

        /**
         * Gets the value of the x property.
         * 
         * @return
         *     possible object is
         *     {@link String }
         *     
         */
        public String getX() {
            return x;
        }

        /**
         * Sets the value of the x property.
         * 
         * @param value
         *     allowed object is
         *     {@link String }
         *     
         */
        public void setX(String value) {
            this.x = value;
        }

        /**
         * Gets the value of the y property.
         * 
         * @return
         *     possible object is
         *     {@link String }
         *     
         */
        public String getY() {
            return y;
        }

        /**
         * Sets the value of the y property.
         * 
         * @param value
         *     allowed object is
         *     {@link String }
         *     
         */
        public void setY(String value) {
            this.y = value;
        }

        /**
         * Gets the value of the z property.
         * 
         * @return
         *     possible object is
         *     {@link String }
         *     
         */
        public String getZ() {
            return z;
        }

        /**
         * Sets the value of the z property.
         * 
         * @param value
         *     allowed object is
         *     {@link String }
         *     
         */
        public void setZ(String value) {
            this.z = value;
        }

        /**
         * Gets the value of the seed property.
         * 
         * @return
         *     possible object is
         *     {@link String }
         *     
         */
        public String getSeed() {
            return seed;
        }

        /**
         * Sets the value of the seed property.
         * 
         * @param value
         *     allowed object is
         *     {@link String }
         *     
         */
        public void setSeed(String value) {
            this.seed = value;
        }

    }

}
